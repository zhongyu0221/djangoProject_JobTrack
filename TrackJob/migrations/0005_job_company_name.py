# Generated by Django 4.0.3 on 2022-07-19 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrackJob', '0004_rename_job_jd_job_job_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Company_Name',
            field=models.CharField(default=1231, max_length=120),
            preserve_default=False,
        ),
    ]
