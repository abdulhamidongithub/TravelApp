from django.contrib.auth.models import User
from django.db import models

class Vehicle(models.Model):
    name = models.CharField(max_length=30, blank=True)
    reg_num = models.IntegerField()

    def __str__(self):
        return f"{self.reg_num}"

class Passenger(models.Model):
    name = models.CharField(max_length=30)
    driver = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Journey(models.Model):
    date_and_time = models.DateTimeField(auto_now_add=True)
    distance = models.FloatField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, related_name="kilometers")
    driver = models.ForeignKey(Passenger, on_delete=models.SET_NULL, null=True)
    passengers = models.ManyToManyField(Passenger, related_name="journeys")

