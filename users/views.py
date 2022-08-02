
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from .forms import RegisterForm

def login_view(request,*args,**kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You are loged in!')
            return redirect ('login')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, 'Unable to login')
            return redirect('login')

    return render(request, "auth/login.html", {})





def register_view(response):
    form = RegisterForm(response.POST)
    if response.method == "POST" or None:
        if form.is_valid():
            form.save()

            return redirect("/login")
        else:
            form = RegisterForm()

    return render(response, "register/register.html", {"form":form})