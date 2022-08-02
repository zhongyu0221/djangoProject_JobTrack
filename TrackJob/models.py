from django.db import models

# Create your models here.



class Job(models.Model):

    #Blank: How the field is rendered (F = Requied Field, NULL: DB)
    Job_Title = models.CharField(max_length=120) # required to have maxlength
    Company_Name = models.CharField(max_length=120)
    SkillType = [('Python', 'Python'), ('Java', 'Java'), ('SQL', 'SQL'), ('HTML', 'HTML/CSS'),('Other','Other') ]  # enum
    Required_Skills = models.CharField(blank=True, choices=SkillType, max_length=10)
    Job_Description = models.TextField()
    Submitted_Date = models.DateField()
    Note = models.TextField(blank=False, null=True)







