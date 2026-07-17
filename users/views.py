from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

from users.forms import UserRegisterForm, UserLoginForm, UserUpdateForm


def user_register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            # print(form.cleaned_data['password'])
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return HttpResponseRedirect(reverse('users:user_login'))
    context = {
        'title': 'Создать аккаунт',
        'form': UserRegisterForm
    }
    return render(request, 'users/register.html', context=context)


def user_login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(email=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('dogs:index'))
                else:
                    return HttpResponse('Аккаунт неактивен!')
    context = {
        'title': 'Авторизация',
        'form': UserLoginForm
    }
    return render(request, 'users/login.html', context=context)

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


def user_profile_view(request):
    user_object = request.user
    context = {
        'title': f'Ваш профиль {user_object}'
    }
    return render(request, 'users/user_profile_read_only.html', context=context)


def user_update_view(request):
    user_object = request.user
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=user_object)
        if form.is_valid():
            user_object = form.save()
            user_object.save()
            return HttpResponseRedirect(reverse('users:user_profile'))
    context = {
        'object': user_object,
        'title': f'Изменить профиль {user_object}',
        'form': UserUpdateForm(instance=user_object),
    }
    return render(request, 'users/register_update.html', context=context)


def user_logout_view(request):
    logout(request)
    return redirect('dogs:index')