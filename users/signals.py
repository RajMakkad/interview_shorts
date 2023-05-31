# This module is used to create and save Profile object as soon as an User object is created and saved in the django.
# post_save signal is triggered when an object is saved in django.
from django.db.models.signals import post_save 

# User is gonna send the signal when an user object will be created.
from django.contrib.auth.models import User

# receiver is gonna receive the signal triggred by the user.
from django.dispatch import receiver
from .models import Profile

# `receiver` decorator is gonna receive the `post_save` object create signal triggered by the `user` then in response `create_profile` function will run.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_profile(sender, instance,  **kwargs):
    instance.profile.save()


# After completing this signals.py module, we need to import it in the ready function of this app's apps.py