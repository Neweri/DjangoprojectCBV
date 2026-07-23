import random
import string

from django import forms
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy

from users.models import User
from users.forms import UserRegisterForm, UserLoginForm, UserUpdateForm, UserChangePasswordForm, UserPasswordResetForm,  UserForm
from users.services import send_register_email, send_new_password_email

class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:user_login')
    template_name = 'users/register_update.html'
    extra_context = {
        'title': 'Создать аккаунт'
    }

    def form_valid(self,form):
        self.object = form.save()
        send_register_email(self.object.email)
        return super().form_valid(form)

#def user_register_view(request):
    # if request.method == 'POST':
    #     form = UserRegisterForm(request.POST)
    #     if form.is_valid():
    #         new_user = form.save()
    #         # print(form.cleaned_data['password'])
    #         new_user.set_password(form.cleaned_data['password'])
    #         new_user.save()
    #         send_register_email(new_user.email)
    #         return HttpResponseRedirect(reverse('users:user_login'))
    # context = {
    #     'title': 'Создать аккаунт',
    #     'form': UserRegisterForm
    # }
    # return render(request, 'users/register_update.html', context=context)

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    extra_context = {
        'title': 'Авторизация'
    }

#def user_login_view(request):
    # if request.method == 'POST':
    #     form = UserLoginForm(request.POST)
    #     if form.is_valid():
    #         cd = form.cleaned_data
    #         user = authenticate(email=cd['email'], password=cd['password'])
    #         if user is not None:
    #             if user.is_active:
    #                 login(request, user)
    #                 return HttpResponseRedirect(reverse('dogs:index'))
    #             return HttpResponse('Аккаунт неактивен!')
    #         return HttpResponse('Нет такого пользователя')
    # context = {
    #     'title': 'Авторизация',
    #     'form': UserLoginForm
    # }
    # return render(request, 'users/login.html', context=context)

# если в БД нет значения по умолчанию
#def user_profile_view(request):
#    user_object = request.user
#    if user_object.first_name and user_object.last_name:
#        user_name = user_object.first_name + ' ' + user_object.last_name
#    else:
#        user_name = 'Anonymous'
#    context = {
#        'title': f'Ваш профиль {user_name}'
#    }
#    return render(request, 'users/user_profile_read_only.html', context=context)


class UserProfileView(DetailView):
    model = User
    form_class = UserForm
    template_name = 'users/user_profile_read_only.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        user_obj = self.get_object()
        context_data['title'] = f'Профиль пользователя {user_obj}'
        return context_data

#"@login_required(login_url='users:user_login')
# def user_profile_view(request):
#     user_object = request.user
#     context = {
#         'title': f'Ваш профиль {user_object}'
#     }
#     return render(request, 'users/user_profile_read_only.html', context=context)

class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/register_update.html'
    success_url = reverse_lazy('users:user_profile')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        user_obj = self.get_object()
        context_data['title'] = f'Изменить профиль: {user_obj}'
        return context_data

#"@login_required(login_url='users:user_login')
# def user_update_view(request):
#     user_object = request.user
#     if request.method == 'POST':
#         form = UserUpdateForm(request.POST, request.FILES, instance=user_object)
#         if form.is_valid():
#             user_object = form.save()
#             user_object.save()
#             return HttpResponseRedirect(reverse('users:user_profile'))
#     context = {
#         'object': user_object,
#         'title': f'Изменить профиль {user_object}',
#         'form': UserUpdateForm(instance=user_object),
#     }
#     return render(request, 'users/register_update.html', context=context)


class UserPasswordChangeView(PasswordChangeView):
    form_class = UserChangePasswordForm
    template_name = 'users/change_password.html'
    success_url = reverse_lazy('users:user_profile')
    extra_context = {
        'title': 'Изменить пароль'
    }

#@login_required(login_url='users:user_login')
# def user_change_password_view(request):
#     user_object = request.user
#     form = UserChangePasswordForm(user_object, request.POST)
#     if request.method == 'POST':
#         if form.is_valid():
#             user_object = form.save()
#             update_session_auth_hash(request, user_object)
#             messages.success(request, 'Пароль был успешно изменен!')
#             return HttpResponseRedirect(reverse('users:user_profile'))
#         else:
#             messages.error(request, 'Не удалось изменить пароль!')
#     context = {
#         'form': form,
#         'title': f'Изменить пароль {user_object}'
#     }
#     return render(request, 'users/change_password.html', context)


class UserLogoutView(LogoutView):
    template_name = 'users/logout.html'
    extra_context = {
        'title': 'Выход из аккаунта'
    }

#def user_logout_view(request):
    # logout(request)
    # return redirect('dogs:index')


def user_generate_new_password_view(request):
    new_password = ''.join(random.sample(string.ascii_letters + string.digits, k=12))
    request.user.set_password(new_password)
    request.user.save()
    send_new_password_email(request.user.email, new_password)
    return redirect(reverse('dogs:index'))


def user_password_reset_view(request):
    if request.method == 'POST':
        form = UserPasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            new_password = ''.join(random.sample(string.ascii_letters + string.digits, k=12))
            try:
                user = User.objects.get(email=email)
                user.set_password(new_password)
                user.save()
                send_new_password_email(email, new_password)
                messages.success(
                    request,
                    f'Новый пароль отправлен на почту {email}. Проверьте вашу почту!'
                )
                return redirect('users:user_login')
            except forms.ValidationError:
                messages.error(request, 'Пользователь с таким email не найден!')
                return redirect('users:reset_password')
    else:
        form = UserPasswordResetForm()
    context = {
        'title': 'Восстановление пароля',
        'form': form
    }
    return render(request, 'users/reset_password.html', context=context)
