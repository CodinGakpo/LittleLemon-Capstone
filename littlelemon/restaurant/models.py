from django.db import models
from django.utils import timezone
# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Booking(models.Model):
    title = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    Booking_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title