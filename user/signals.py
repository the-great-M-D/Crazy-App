
# singal shit hacking it again
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from accounts.models import Account


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print('Creating Profile Now With The Post Save Signal !!!!!!!!!!!!!!!!')
    if created:
        Profile.objects.create(user=instance)
        Account.objects.create(user=instance)
        
        
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    instance.account.save()
    print(f'hopefull we have saved this profile => {instance.profile}')