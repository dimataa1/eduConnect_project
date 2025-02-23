import os

from cloudinary.models import CloudinaryField
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )

    email = models.EmailField(unique=True)

    username = models.CharField(
        max_length=100,
        unique=True,
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='student',
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    is_approved = models.BooleanField(
        default=False,
        help_text=_("Designates whether the teacher account is approved by an admin."),
    )

    objects = AppUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        related_name='profile',
    )

    age = models.IntegerField(
        blank=True,
        null=True,
    )

    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=30,
    )

    grade = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="",
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    subject = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="",
    )

    profile_picture = CloudinaryField(
        'profile_picture_image',
        blank=True,
        null=True,
        default="https://res.cloudinary.com/dmsakestc/image/upload/v1740333445/Default_pfp.svg_gavlli.png",
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.user.email}"

    def save(self, *args, **kwargs):
        if self.user.role == 'student':
            self.subject = None
        elif self.user.role == 'teacher':
            self.grade = None

        super().save(*args, **kwargs)

    def clean(self):

        if self.user.role == 'student' and self.subject:
            raise ValidationError("Students cannot have a subject.")

        if self.user.role == 'teacher' and self.grade:
            raise ValidationError("Teachers cannot have a grade.")

    def delete_profile_picture(self):

        if self.profile_picture and hasattr(self.profile_picture, 'path') and os.path.isfile(self.profile_picture.path):
            os.remove(self.profile_picture.path)

        self.profile_picture = None
        self.save()

    def restore_default_picture(self):

        self.delete_profile_picture()
        self.profile_picture = 'https://res.cloudinary.com/dmsakestc/image/upload/v1740333445/Default_pfp.svg_gavlli.png'
        self.save()