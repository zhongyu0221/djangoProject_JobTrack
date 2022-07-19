from django.db import models

# Create your models here.
class Job(models.Model):

    #Blank: How the field is rendered (F = Requied Field, NULL: DB)
    Job_Title = models.CharField(max_length=120) # required to have maxlength
    Job_Description = models.TextField()
    Company_Name = models.CharField(max_length=120)

    #applied = models.BooleanField(default=True)
    Submitted_Date = models.CharField(max_length=120)
    Note = models.TextField(blank=False, null=True)
    Required_Skills = models.TextField(default='Replace with Coding Skills')




