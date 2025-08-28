from django.shortcuts import render, redirect
from .models import User

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
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
    return render(request, 'users/sign_in.html')