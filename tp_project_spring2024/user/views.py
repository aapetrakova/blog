from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import RegisterForm, LogInForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.contrib import messages


class RegisterView(View):
    """View for registering a new user."""
    def get(self, request, *args, **kwargs):
        """GET request for register user

        :param request: GET request
        :param args:
        :param kwargs:
        :return: redirects to register page
        """
        form = RegisterForm()
        return render(request, 'user/register.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        """POST request for register user

        :param request: POST request
        :param args:
        :param kwargs:
        :return: redirects to login page
        """
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'user/register.html', context={
            'form': form,
        })


class LoginView(View):
    """View for logging in."""
    def get(self, request, *args, **kwargs):
        """GET request for logging in

        :param request: GET request
        :param args:
        :param kwargs:
        :return: login form
        """
        form = LogInForm()
        return render(request, 'user/login.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        """
        POST request for logging in.

        :param request: POST request
        :param args:
        :param kwargs:
        :return: logged in user
        """
        form = LogInForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'user/login.html', context={
            'form': form,
        })


def logoutUser(request):
    """
    Function for logout user

    :param request:
    :return: login page
    """
    logout(request)
    messages.info(request, 'Вы вышли из учетной записи')
    return redirect('login')
