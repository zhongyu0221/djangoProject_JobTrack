from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Job
from .forms import JobForm

def home_view(request, *args, **kwargs):
    return render(request,"homepage.html",{})



def login_view(request,*args, **kwargs):
    readme = {
        "sumamry": "This is a Job Hunting Tracker App powered by Django",
        "contact": "Contact me at zhongyu0221@gmail.com",
        "mylist":[123,323,1231]
    }
    return render(request,"loginpage.html",readme)


def register_view(request,*args, **kwargs):
    return render(request,"registerpage.html",{})


def showrecord_view(request,*args, **kwargs):
    queryset = Job.objects.all() #list of objects
    context = {
        "object_list": queryset
    }
    return render(request,"showrecordpage.html",context)


#Render model here. Dynamic URL
def job_detail_view(request, id):
    #obj = Job.objects.get(id = id)
    obj = get_object_or_404(Job,id = id)

    context = {
        "object" :obj
    }
    return render(request,'job/jobdetail.html',context)


# Using Form

def job_add_view(request):
    form = JobForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = JobForm() #re-render it after save

    context = {
        'form':form
    }
    return render(request,'job/job_create.html',context)