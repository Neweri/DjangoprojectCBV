from django import forms
from django.contrib.auth.forms import PasswordChangeForm

from users.models import User
from users.validators import validate_password
from dogs.forms import StyleFormMixin


class UserForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone')


class UserRegisterForm(StyleFormMixin, forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        cd = self.cleaned_data
        validate_password(cd['password'])
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Ошибка! Пароли не совпадают!')
        return cd['password2']


class UserLoginForm(StyleFormMixin, forms.Form):
    email = forms.EmailField(label='email')
    password = forms.CharField(label='пароль', widget=forms.PasswordInput)


class UserUpdateForm(UserForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'telegram', 'avatar')


class UserPasswordResetForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        max_length=254,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите ваш email'
        })
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email не найден!')
        return email

class UserChangePasswordForm(StyleFormMixin, PasswordChangeForm):
    pass