from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
# Create your views here.
from .models import Job
from .forms import JobForm
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required
#
# def home_view(request, *args, **kwargs):
#     return render(requst,"homepage.html",{})

class homeview(View):
    def get(self,request,*args,**kwargs):
        return render(request,"homepage.html",{})



@login_required
def showrecord_view(request, *args, **kwargs):
#     queryset = Job.objects.all() #list of objects

    user_record_queryset = Job.objects.filter(user = request.user)
    context = {
        "object_list": user_record_queryset
    }
    return render(request, "showrecordpage.html", context)



# Using Form

def job_add_view(request):
    # form = JobForm(request.POST or None) #uncleaned data
    # if request == 'POST':
    form = JobForm()

    context = {
        'form': form
    }
    if request.method =='POST':
        form = JobForm(request.POST)
        context['form'] = form

        if  form.is_valid(): #form is cleaned
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request,('Successfully Saved Record'))
            form = JobForm() #re-render it after save

        else:
            messages.success(request, ('Please fill all the fields'))
            form = JobForm() #re-render it after save


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

