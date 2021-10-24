from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Advisor(models.Model):
    advisor_name = models.CharField(max_length=50)
    advisor_photo_url = models.URLField(max_length=200)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_time = models.DateTimeField()
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE)

