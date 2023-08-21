from django.shortcuts import render


def signupuser(request):
    return render(request, 'todo/signup.html')


def current_todos(request):
    return render(request, 'todo/current_todos.html')
