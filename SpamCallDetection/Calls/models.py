from django.db import models

# Create your models here.

class PhoneNumber(models.Model):
    number = models.CharField(max_length=15, unique=True)
    is_spam = models.BooleanField(default=False)
    owner_name = models.CharField(max_length=150, null=True, blank=True)
    image = models.ImageField(upload_to='phone_images/', null=True, blank=True)

    def __str__(self):
        return self.number   

 
