# Generated by Django 5.1.3 on 2024-12-26 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='default/default_pfp', help_text='Upload a profile picture.', null=True, upload_to='static/profile_images/'),
        ),
    ]
