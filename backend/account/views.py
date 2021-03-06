from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm, PasswordEditForm
from .models import Profile


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password']
            )
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Authenticated successfully')
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    if request.user:
        return render(request, 'account/dashboard.html', {'section': 'dashboard', 'profile': Profile.objects.get(user=request.user)})
    else:
        user_login(request)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Создаем нового пользователя, но пока не сохраняем в базу данных.
            new_user = user_form.save(commit=False)
            # Задаем пользоветелю зашифрованный пароль.
            new_user.set_password(user_form.cleaned_data['password'])
            # Сохраняем пользователя в базе данных
            new_user.save()
            # Создаем пустой профиль для пользователя
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})

@login_required
def edit(request):
    password_form = PasswordEditForm(instance=request.user)
    user_form = UserEditForm(instance=request.user)
    profile_form = ProfileEditForm(instance=request.user.profile)
    if request.method == 'POST':
        if 'change_password' in request.POST:
            password_form = PasswordEditForm(instance=request.user, data=request.POST)
            if password_form.is_valid():
                request.user.set_password(password_form.cleaned_data['password'])
                messages.success(request, 'Password updated successfully')
        elif 'save_changes' in request.POST:
            profile_form = ProfileEditForm(instance=request.user.profile,
                                           data=request.POST,
                                           files=request.FILES)
            user_form = UserEditForm(instance=request.user, data=request.POST)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    return render(request, 'account/edit.html', {'password_form': password_form, 'user_form': user_form, 'profile_form': profile_form})
