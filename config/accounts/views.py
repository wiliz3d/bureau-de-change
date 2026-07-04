from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

from .forms import LoginForm


class UserLoginView(LoginView):
    template_name = "accounts/login.html"
    authentication_form = LoginForm


def logout_view(request):
    logout(request)
    return redirect("home")