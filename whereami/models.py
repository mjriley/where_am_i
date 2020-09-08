# from datetime import date
from django.utils import timezone
from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    profile_picture = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    def get_current_location(self):
        return Location.objects.filter(user=self.id, current=True).first()

    def update_location(self, location):
        # Ensure this is a transaction
        # Fetch the current location
        prev_location = self.get_current_location()
        # If it exists, make it no longer current
        if prev_location:
            prev_location.current = False
            prev_location.save()

        # Insert the new location as current
        return Location.objects.create(user=self, city_name=location['name'], country_name=location['country'],
                                       latitude=location['latitude'], longitude=location['longitude'])


class Location(models.Model):
    city_name = models.CharField(max_length=100)
    country_name = models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    current = models.BooleanField(default=True)
    time = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.city_name}, {self.country_name} ({self.latitude}, {self.longitude})'
