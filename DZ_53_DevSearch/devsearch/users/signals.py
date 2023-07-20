from django.db.models.signals import post_save, post_delete
from django.dispatch.dispatcher import receiver
from .models import Profile, User
@receiver(post_save, sender=User)
def profile_update(sender, instance, created, **kwargs):
    print('User signal!')
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )

@receiver(post_delete, sender=Profile)
def profile_delete(sender, instance, **kwargs):
    user = instance.user
    user.delete()

# post_save.connect(profile_update, sender=Profile)
# post_delete.connect(profile_delete, sender=Profile)