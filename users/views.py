from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
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