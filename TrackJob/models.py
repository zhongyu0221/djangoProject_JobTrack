from django.db import models

# Create your models here.
class Job(models.Model):

    #Blank: How the field is rendered (F = Requied Field, NULL: DB)
    Job_title = models.CharField(max_length=120) # required to have maxlength
    Job_JD = models.TextField()
    #applied = models.BooleanField(default=True)
    Submitted_Date = models.TextField(default='Replace with a Date')
    TakehomePoint = models.TextField(blank=False, null=True)
    RequiredSkills = models.TextField(default='Replace with Coding Skills')




