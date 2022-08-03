from django import forms
from .models import Job
from django.core.exceptions import ValidationError


class DateInput(forms.DateInput):
    input_type = 'date'


class JobForm(forms.ModelForm):
    #Job_title = forms.CharField(label = 'Title',widget = forms.TextInput(attrs={"palceholder":"YOur title"}))

    Job_Title = forms.CharField(max_length=120)  # required to have maxlength
    Company_Name = forms.CharField(max_length=120)
    Job_Description = forms.TextInput()
    Note = forms.TextInput()

    def clean_Job_Title(self, *args, **kwargs):
        print('am i not run it at all?')
        clean_data = self.cleaned_data  # distionay contains all fields
        Job_Title = clean_data.get('Job_Title')
        print(Job_Title)

        if "haha" in Job_Title:
            print('validation error noted')
            raise forms.ValidationError('you cannot have haha in your form')
        else:
            return Job_Title


    class Meta:
        model = Job
        exclude = ["user"]
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

# form data clean up in From.py - custorm validation data








