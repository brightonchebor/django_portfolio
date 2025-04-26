from django.shortcuts import render, redirect
from .models import ContactMe
from django.contrib import messages


def home(request):
    context = {}

    return render(request, 'home.html', context)

def login(request):
    context = {}

    return render(request, 'login.html', context)

def my_messages(request):
    context = {}

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
        messages.success(request, 'Thank you for getting in touch, Our support team will respond shortly!')
        return redirect('home')

    else:
        return render(request, 'contact.html')
    
    

def about(request):
    context = {}

    return render(request, 'about.html', context)

def logout(request):
    context = {}

    return render(request, 'logout.html')