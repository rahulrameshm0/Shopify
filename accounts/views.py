from django.shortcuts import render

# Create your views here.

def signin(request):
    return render(request, 'account-section/signin.html')

def register(request):
    return render(request, 'account-section/register.html')

def email_verification(request):
    return render(request, 'account-section/email-varification.html')