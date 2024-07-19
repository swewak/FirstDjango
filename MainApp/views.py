from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import logout
from .forms import UserRegistrationForm

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        print("username =", username)
        print("password =", password)
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            # Return error message
            pass
    return redirect('home')

def home(request):
    return render(request, 'MainApp/index.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    #return render(request, 'MainApp/register.html', {'form': form})