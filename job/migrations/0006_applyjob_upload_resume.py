# Generated by Django 5.1.6 on 2025-03-07 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_remove_job_state_delete_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyjob',
            name='upload_resume',
            field=models.FileField(blank=True, null=True, upload_to='resumes/'),
        ),
    ]
