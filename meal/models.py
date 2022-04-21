from logging import _FormatStyle
from django.db import models
from .models import Profile

# Create your models here.

class Oder(models.Model):
    ref_code = models.CharField(max_length=20)
    user = models.OneToOneField(on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=_FormatStyle)
    date_orderd = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)

    def get_cart_item(self):
        return self.item.all()

    def __str__(self):
        return self.owner, self.ref_code