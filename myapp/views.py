from django.shortcuts import render


def home(request):
    context = {}

    return render(request, 'base.html', context)

def login(request):
    context = {}

    return render(request, 'login.html', context)

def messages(request):
    context = {}

    return render(request, 'messages.html', context)

def contact(request):
    context = {}

    return render(request, 'contact.html', context)

def about(request):
    context = {}

    return render(request, 'about.html', context)

def logout(request):
    context = {}

    return render(request, 'logout.html')