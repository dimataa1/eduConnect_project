# Generated by Django 4.2.19 on 2025-03-09 10:54

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_alter_post_image_alter_school_image_alter_tour_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default='https://res.cloudinary.com/dmsakestc/image/upload/v1740333648/default_pic_ouvlzx.png', max_length=255, null=True, verbose_name='post_image'),
        ),
        migrations.AlterField(
            model_name='school',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default='https://res.cloudinary.com/dmsakestc/image/upload/v1740333648/default_pic_ouvlzx.png', max_length=255, null=True, verbose_name='school_image'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default='https://res.cloudinary.com/dmsakestc/image/upload/v1740333648/default_pic_ouvlzx.png', max_length=255, null=True, verbose_name='tour_image'),
        ),
    ]
