from django.contrib.auth.models import User
from django.db import models


class Flight(models.Model):
    destination = models.CharField(max_length=100)
    time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    miles = models.PositiveIntegerField()

    def __str__(self):
        return f"to {self.destination} at {self.time}"


class Booking(models.Model):
    flight = models.ForeignKey(
        Flight, on_delete=models.CASCADE, related_name="bookings"
    )
    date = models.DateField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings")
    passengers = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username}: {self.flight}"


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username}"
