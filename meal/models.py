from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
from phone_field import PhoneField
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=400, blank=True)
    name = models.CharField(blank=True,max_length=120)
    profile_pic = CloudinaryField('profile_pic')
    phone_number = PhoneField(max_length=15, blank = True)

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Oder(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=400, blank=True)
    date_ordered = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image')

    def get_cart_item(self):
        return self.item.all()

    def __str__(self):
        return self.owner, self.ref_code
