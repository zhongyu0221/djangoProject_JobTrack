from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
# Create your views here.
from .models import Job
from .forms import JobForm
from django.contrib import messages

def home_view(request, *args, **kwargs):
    return render(request,"homepage.html",{})



def showrecord_view(request,*args, **kwargs):
    queryset = Job.objects.all() #list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "showrecordpage.html", context)



# Using Form

def job_add_view(request):
    form = JobForm(request.POST or None)
    # if request == 'POST':
    if  form.is_valid():
        form.save()
        messages.success(request,('Successfully Saved Record'))
        form = JobForm() #re-render it after save

    else:
        messages.success(request, ('Please fill all the fields'))
        form = JobForm() #re-render it after save

    context = {
        'form':form
    }

    return render(request, 'job_create.html', context)


def job_update_view (request,id):
    obj = Job.objects.get(id = id)
    form = JobForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/TrackJob/showrecord')

    context = {
        "object":obj,
        "form":form
    }

    return render(request, 'job_update.html', context)



def job_delete_view (request,id):
    obj = Job.objects.get(id = id)
    obj.delete()
    messages.success(request,('Sucecsful delete the record'))

    return redirect('/TrackJob/showrecord')
#python manage.py flush reset database



def job_search_view (request):
    if request.method =='POST':
        searchfield = request.POST['searchfield']
        searcresult = Job.objects.filter(Job_Title__contains=searchfield)


        return render(request,'job_search.html',{'searchfield':searchfield,'searcresult':searcresult})
    else:
        return render(request,'job_search.html',{})