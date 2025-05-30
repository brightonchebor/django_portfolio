from django.shortcuts import render, redirect
from .models import ContactMe
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
    context = {}

    return render(request, 'home.html', context)

def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            messages.success(
                request,
                'You are now logged in'
            )
            return redirect('messages')
        else:
            messages.error(
                request,
                'Invalid login credentials'
            )    
    return render(request, 'login.html', context={})

def my_messages(request):

    texts = ContactMe.objects.all()
    context = {
        'texts' : texts
    }

    return render(request, 'messages.html', context)

def contact(request):

    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        name = request.POST['name']

        contact = ContactMe.objects.create(
            subject = subject,
            email = email,
            message = message,
            name = name

        ) 
        contact.save()  
        messages.success(request, 'Thank you for getting in touch, will respond shortly!')
        return redirect('home')

    else:
        return render(request, 'contact.html')
    
    

def about(request):
    context = {}

    return render(request, 'about.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect('home')