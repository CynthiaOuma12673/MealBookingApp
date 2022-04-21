from django.db import models
from django.db import models
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.



class Profile(models.Model):
    profile_pic = CloudinaryField('image')
    