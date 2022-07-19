from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    #Job_title = forms.CharField(label = 'Title',widget = forms.TextInput(attrs={"palceholder":"YOur title"}))



    class Meta:
        model = Job
        fields = [
            'Job_Title',
            'Job_Description',
            'Company_Name',
            'Submitted_Date',
            'Note',
            'Required_Skills',

        ]


