from django.shortcuts import render, redirect, get_object_or_404
from app.models.bank import *
from .form import BankForm
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
import json
from django.db.models import Q
from django.db import connection
from django.contrib.humanize.templatetags.humanize import intcomma
from django.template.defaultfilters import floatformat
from app.view.system.company.company import filterCompaniesId
from app.view.system.data_domain.data_domain import getCompaniesId, permission


def index(request, template_name='financial/master/banks/list.html'):
    data_domain_company = getCompaniesId(request)
    companies_id = data_domain_company['companies_id']
    filter_company_id = filterCompaniesId(companies_id)

    context = {
        'title': 'Cash/Banks',
        'banks': Bank.objects.filter(filter_company_id).order_by('bank_name'),
        # 'urldefault' : '/master/',
        'menu': 'financial',
        'submenu': 'setup',
        'active': 'bank'
    }

    return render(request, template_name, context)


def add(request, template_name='financial/master/banks/form.html'):
    data_domain_company = getCompaniesId(request)
    def_company_id = data_domain_company['def_company_id']

    if def_company_id is None or def_company_id == "":
        messages.error(request, "can't create data, choose default company in data domain")
        return redirect('banks')

    if request.method == 'POST':
        form = BankForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'bank Added Successfully')
            return redirect('banks')
        else:
            print(form.errors)
    else:
        form = BankForm()

    context = {
        'title': 'Cash/Bank Form',
        'form': BankForm(),
        'menu': 'financial',
        'submenu': 'setup',
        'active': 'bank'
    }
    return render(request, 'financial/master/banks/form.html', context)


def edit(request, bank_id):
    rst = get_object_or_404(Bank, bank_id=bank_id)

    check_permission = permission(request, rst.company_id)
    if check_permission == 0:
        return redirect('forbidden_access')

    if request.method == 'POST':
        form = BankForm(request.POST, instance=rst)
        if form.is_valid():
            obj = form.save(commit=False)
            if request.POST.get('cash') == None:
                obj.cash = 0;
            obj.save()

            messages.success(request, 'bank updated Successfully')
            return redirect('banks')

    form = BankForm(instance=rst)
    context = {
        'title': 'Cash/Bank Form',
        'form': form,
        'menu': 'financial',
        'submenu': 'setup',
        'active': 'bank',
        'cb': rst,
    }
    return render(request, 'financial/master/banks/form.html', context)


def delete(request, bank_id):
    rst = Bank.objects.get(bank_id=bank_id)

    check_permission = permission(request, str(rst.company_id))
    if check_permission == 0:
        return redirect('forbidden_access')

    rst.delete()
    messages.success(request, 'bank deleted')
    return redirect('banks')


def loadBank(request):
    data_domain_company = getCompaniesId(request)
    companies_id = data_domain_company['companies_id']
    filter_company_id = filterCompaniesId(companies_id)
    company_id = request.GET.get('company_id')
    bank_group_id = request.GET.get('bank_group_id')

    search = request.GET.get('q')
    if search:
        company_banks = Bank.objects.filter(filter_company_id, bank_name__icontains=search)
        global_banks = Bank.objects.filter(company_id_isnull=True, bank_name_icontains=search)
    else:
        company_banks = Bank.objects.filter(filter_company_id).order_by('bank_name')
        global_banks = Bank.objects.filter(company_id__isnull=True).order_by('bank_name')

    if company_id:
        company_banks = company_banks.filter(company_id=company_id)

    if bank_group_id:
        company_banks = company_banks.filter(bank_group_id=bank_group_id)

    company_banks = company_banks[:20].values('bank_name', 'bank_id')
    global_banks = global_banks[:20].values('bank_name', 'bank_id')

    data = {}

    lists = []
    if company_banks is not None:
        for dt in company_banks:
            lists.append({
                'id': dt['bank_id'],
                'text': dt['bank_name'],
            })

    if global_banks is not None:
        for dt in global_banks:
            lists.append({
                'id': dt['bank_id'],
                'text': dt['bank_name'],
            })

    data['results'] = lists
    test = json.dumps(data)
    return HttpResponse(test, content_type='application/json')


def loadDataDomainBank(request):
    search = request.GET.get('q')
    banks_id = request.GET.get('banks_id')
    # convert to array val integer
    banks_id = [int(x) for x in banks_id.split(",")]

    if search:
        bank = Bank.objects.filter(bank_name_icontains=search, bank_id_in=banks_id).order_by('bank_name')[:20]
    else:
        bank = Bank.objects.filter(bank_id__in=banks_id).order_by('bank_name')[:20]

    data = {}

    lists = []
    for dt in bank:
        lists.append({
            'id': dt.bank_id,
            'text': dt.bank_name,
        })

    data['results'] = lists
    test = json.dumps(data)
    return HttpResponse(test, content_type='application/json')


def bankData(request, bank_id):
    if bank_id is None:
        bank_id = 0

    bank = Bank.objects.filter(bank_id=bank_id).first()
    data = []
    if bank is not None:
        data = {
            'company_name': bank.company.company_name,
            'company_id': bank.company_id,
            'cash': bank.cash
        }
    else:
        data = data

    return JsonResponse(data, safe=False)


def loadBankGroup(request):
    bank_groups = BankGroup.objects.all().order_by('group_name')
    data = {}

    lists = []
    if bank_groups is not None:
        for dt in bank_groups:
            lists.append({
                'id': dt.bank_group_id,
                'text': dt.group_name,
            })

    data['results'] = lists
    test = json.dumps(data)
    return HttpResponse(test, content_type='application/json')


def filter_bank_groups(bank_groups_id):
    filter_bank_group_id = Q(bank_group_id=0)

    if bank_groups_id is not None:
        if bank_groups_id != "*":
            bank_group_id = [int(x) for x in bank_groups_id.split(",")]
            filter_bank_group_id = Q(bank_group_id__in=bank_group_id)
        else:
            filter_bank_group_id = Q(company_id_isnull=False) | Q(company_id_isnull=True)

    return filter_bank_group_id


def ajax_get_bank_info(request):
    bank_id = request.GET.get('bank_id')

    if bank_id:
        bank = Bank.objects.get(pk=bank_id)
        balance_amount = 0

        cursor = connection.cursor()
        cursor.execute('select get_bank_balance(%s, %s)', [bank.company_id, bank_id])
        row = cursor.fetchone()

        if row is not None:
            balance_amount = row[0]

        content = {
            'bank_name': bank.bank_name,
            'balance_amount': bank.currency.symbol + " " + intcomma(floatformat(balance_amount, 2))
        }

        json_result = json.dumps(content)
        return HttpResponse(json_result, content_type='application/json')
