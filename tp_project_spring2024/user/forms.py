from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class RegisterForm(forms.Form):
    """Form for registering a new user.

    atribute:username: CharField - user's username.'
    atribute:password: CharField - user's password.'
    atribute:repeat_password: CharField - user's repeat password.'
    atribute:email: EmailField - user's email address.'
    """

    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "inputUsername",
            'type': 'username',
            'placeholder': 'Имя пользователя',
        }),
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'id': "inputPassword",
            'type': 'password',
            'placeholder': 'Пароль'
        }),
    )

    repeat_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'id': "ReInputPassword",
            'type': 'password',
            'placeholder': 'Повторите пароль'
        }),
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': "form-control",
            'id': "inputEmail",
            'type': 'email',
            'placeholder': 'Введите email'
        }),
    )

    def clean(self):
        """

        :return: raise, if password and repeat_password not match, else path
        """
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['repeat_password']

        if password != confirm_password:
            raise forms.ValidationError(
                "Пароли не совпадают"
            )

    def save(self):
        """

        :return: authenticated user
        """
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
        user.save()
        auth = authenticate(**self.cleaned_data)
        return auth


class LogInForm(forms.Form):
    """
    Form for logging in.

    atribute:username: CharField - user's username.'
    atribute:password: CharField - user's password.'
    """
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "inputUsername",
        })
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control mt-2",
            'id': "inputPassword",
        })
    )