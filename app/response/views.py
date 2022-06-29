from django.shortcuts import render

# Create your views here.
def page404(request):
    return render(request, "Response/404.html")
