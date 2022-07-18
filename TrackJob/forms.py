from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    #Job_title = forms.CharField(label = 'Title',widget = forms.TextInput(attrs={"palceholder":"YOur title"}))



    class Meta:
        model = Job
        fields = [
            'Job_title',
            'Job_JD'

        ]
