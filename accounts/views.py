from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from  django.contrib.auth.models import User
# Create your views here.

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Username or Password is incorrect")
            return redirect('signin')

    return render(request, 'account-section/signin.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        # phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "This username already exits")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "This email address already exists")
            return redirect('register')

        if password != confirm_password:
            messages.error(request, "Password is not matched")
            return redirect('register')

        # if len(phone) < 10:
        #     messages.error(request, "The phone numbers should contain minimum 10 digits!")

        if len(username) < 8:
            messages.error(request, "The length of the username should be more than 8 characters")
            return redirect('register')

        if len(password):
            messages.error(request, "The length of the password should be more than 8 characters")
            return redirect('register')

        create_user = User.objects.create_user(username=username,email=email,password=password)
        create_user.save()
        return redirect('signin')

    return render(request, 'account-section/register.html')

def email_verification(request):
    return render(request, 'account-section/email-varification.html')

def dashboard(request):
    return render(request, 'account-section/dashboard.html')