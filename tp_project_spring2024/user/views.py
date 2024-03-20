from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import RegisterForm, LogInForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'user/register.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
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
    def get(self, request, *args, **kwargs):
        form = LogInForm()
        return render(request, 'user/login.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
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
    logout(request)
    messages.info(request, 'Вы вышли из учетной записи')
    return redirect('login')
