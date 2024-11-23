# Generated by Django 5.1.3 on 2024-11-23 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='points',
        ),
        migrations.AddField(
            model_name='profile',
            name='grade',
            field=models.CharField(blank=True, help_text="Applicable for students. Example: '10th Grade'.", max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='subject',
            field=models.CharField(blank=True, help_text="Applicable for teachers. Example: 'Mathematics'.", max_length=100, null=True),
        ),
    ]
