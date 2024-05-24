from django.db import models
from django.utils.timezone import get_current_timezone

# Create your models here.
class Mail(models.Model):
    email = models.EmailField()
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.email
   