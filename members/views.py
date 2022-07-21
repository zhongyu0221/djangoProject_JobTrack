from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def login_user(request, *args, **kwargs):

    if request.method =='POST':
        username = request.POST['username'] # get from html name
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
            # Redirect to a success page.
        else:
            messages.success(request,('unsuccess login, please try again!!'))
            return redirect('/members/login_user/')

    else:
            return render(request, "authentication/login.html", {})



def logout_user(request, *args,**kwargs):
   logout(request)
   messages.success(request, ('You were logged out!'))

   return redirect('home')






