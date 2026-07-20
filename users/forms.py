from django import forms

from users.models import User
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