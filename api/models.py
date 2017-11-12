from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

@receiver(post_save, sender=User)
def token_handler(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.get_or_create(user=instance)

