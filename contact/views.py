from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.mail import send_mail

def contact_view (request,*args, **kwargs):

    if request.method =='POST':
        txtName= request.POST['txtName'] # get from html name
        txtEmail = request.POST['txtEmail']
        txtPhone = request.POST['txtPhone']
        txtMsg = request.POST['txtMsg']


        # send email
        # send_mail(
        #     txtName,
        #     txtMsg,
        #     txtPhone,
        #     txtEmail,
        #     ['zhongyu0221@gmail.com'],
        # )
        messages.success(request,('Your message is sent'))
        return render(request, 'contactme.html',{'txtMsg':txtMsg})
    else:
        return render(request, 'contactme.html', {})





