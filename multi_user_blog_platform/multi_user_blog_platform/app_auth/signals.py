from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from multi_user_blog_platform.app_auth import models

UserModel = get_user_model()

@receiver(post_save, sender=UserModel)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        models.Pet.objects.create(user=instance)
        instance.pet.save()