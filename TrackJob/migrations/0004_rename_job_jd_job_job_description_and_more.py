# Generated by Django 4.0.3 on 2022-07-19 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrackJob', '0003_job_requiredskills_job_takehomepoint'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='Job_JD',
            new_name='Job_Description',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='Job_title',
            new_name='Job_Title',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='TakehomePoint',
            new_name='Note',
        ),
        migrations.RemoveField(
            model_name='job',
            name='RequiredSkills',
        ),
        migrations.RemoveField(
            model_name='job',
            name='applied',
        ),
        migrations.AddField(
            model_name='job',
            name='Required_Skills',
            field=models.TextField(default='Replace with Coding Skills'),
        ),
        migrations.AlterField(
            model_name='job',
            name='Submitted_Date',
            field=models.CharField(max_length=120),
        ),
    ]
