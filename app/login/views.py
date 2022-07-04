from django.contrib.auth.views import LoginView

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'Login/index.html'
    redirect_authenticated_user = True