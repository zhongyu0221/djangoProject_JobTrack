# Generated by Django 4.0.3 on 2022-07-20 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrackJob', '0005_job_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='Required_Skills',
            field=models.CharField(blank=True, choices=[('Python', 'Python'), ('Java', 'Java'), ('SQL', 'SQL'), ('HTML', 'HTML/CSS')], max_length=10),
        ),
    ]