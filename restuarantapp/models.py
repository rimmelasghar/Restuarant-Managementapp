
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Table(models.Model):
    capacity = models.PositiveBigIntegerField()
    status = models.BooleanField(default=False)


class Booking(models.Model):
    user = models.ForeignKey(User, related_name='bookings',on_delete = models.CASCADE)
    capacity = models.PositiveBigIntegerField()
    time = models.DateTimeField(auto_now_add=True)
    table = models.ForeignKey(Table,on_delete = models.CASCADE, related_name='bookings')
    reservationField= models.DateTimeField()

