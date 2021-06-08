from django.db import models

# Create your models here.
class Motobike(models.Model):
    number_plate = models.IntegerField()
    bike_model = models.CharField(max_length=200)
    warranty = models.IntegerField()
    bike_owner = models.CharField(max_length = 100)

