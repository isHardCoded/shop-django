from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .models import User

def register(request):
    if request.method == 'POST':
        username = request.POST['username'] # tom
        email = request.POST['email']
        password = request.POST['password']

        if username and email and password:
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )

                return redirect('login')

            else:
                error = 'Пользователь с таким именем уже существует'

        else:
             error = 'Заполните все поля'
        return render(request, 'users/sign_up.html', {'error': error})

    return render(request, 'users/sign_up.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('home')

            else:
                error = 'Неправильное имя или пароль'

        else:
            error = 'Заполните все поля'

        return render(request, 'users/sign_in.html', {'error': error})

    return render(request, 'users/sign_in.html')

def logout(request):
    auth_logout(request)
    return redirect('login')

def profile(request, username):
    user = request.user

    return render(request, 'users/profile.html', context={
        'username': username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
    })

@login_required(login_url='login')
def profile_edit(request):
    user = request.user

    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']

        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        user.save()

        return redirect('profile', username=user.username)
    return render(request, 'users/profile_edit.html', context={
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
    })