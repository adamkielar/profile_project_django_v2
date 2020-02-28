from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(default='')
    confirm_email = models.EmailField(default='')
    city = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.CharField(max_length=500, blank=True)
    hobby = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(default='sample.png', upload_to='avatars/')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
