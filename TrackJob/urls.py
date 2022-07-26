from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include

from TrackJob.views import showrecord_view, job_add_view, job_update_view,job_delete_view,job_search_view

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('showrecord/', showrecord_view,name = 'showrecord'),
    path('jobadd/', job_add_view),
    path('jobupdate/<int:id>', job_update_view, name='job_update'),
    path('jobdelete/<int:id>', job_delete_view, name='job_delete'),
    path('jobsearch/', job_search_view, name='job_search'),


]
