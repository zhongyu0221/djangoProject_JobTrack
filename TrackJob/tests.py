from django.test import TestCase
from TrackJob.models import Job


#https://docs.djangoproject.com/zh-hans/4.0/intro/tutorial05/
# Create your tests here.
class JobTestCase(TestCase):
    def setUp(self):
        Job.objects.create(Job_Title="SDE", Required_Skills="Python",Submitted_Date = 2022/12/12)


    def test_job(self):

        software_eng = Job.objects.get(name="SDE")
        self.assertEqual(software_eng.Required_Skills(), 'what is that')








#
#             Job_Title = models.CharField(max_length=120) # required to have maxlength
#     Company_Name = models.CharField(max_length=120)
#     SkillType = [('Python', 'Python'), ('Java', 'Java'), ('SQL', 'SQL'), ('HTML', 'HTML/CSS'),('Other','Other') ]  # enum
#     Required_Skills = models.CharField(blank=True, choices=SkillType, max_length=10)
#     Job_Description = models.TextField()
#     Submitted_Date = models.DateField()
#     Note = models.TextField(blank=False, null=True)