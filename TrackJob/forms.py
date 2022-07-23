from django import forms
from .models import Job



class DateInput(forms.DateInput):
    input_type = 'date'


class JobForm(forms.ModelForm):
    #Job_title = forms.CharField(label = 'Title',widget = forms.TextInput(attrs={"palceholder":"YOur title"}))

    class Meta:
        model = Job
        fields = [
            'Job_Title',
            'Company_Name',
            'Job_Description',
            'Required_Skills',
            'Submitted_Date',
            'Note',
        ]

        widgets = {
            'Submitted_Date': DateInput(),
            'Job_Title': forms.TextInput(attrs = {'class':'form-control'}),
            'Company_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Job_Description': forms.Textarea(attrs={'class': 'form-control'}),
            'Note': forms.Textarea(attrs={'class': 'form-control'}),

        }







