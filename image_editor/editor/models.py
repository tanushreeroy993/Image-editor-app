from django.db import models
from django.utils import timezone
from django.conf import settings



class UserImage(models.Model):
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

