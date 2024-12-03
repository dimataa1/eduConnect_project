from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AppUser, Profile
from .utils import send_welcome_email, send_teacher_approval_email


@receiver(post_save, sender=AppUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        send_welcome_email(instance.email, instance.username)
    else:
        instance.profile.save()


@receiver(post_save, sender=AppUser)
def send_approval_notification(sender, instance, created, **kwargs):

    if not created and instance.is_approved:
        if instance.email:
            send_teacher_approval_email(instance.email, instance.username)
