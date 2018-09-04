from __future__ import unicode_literals
import re
from django.db import models
from ..reglogin.models import User
import datetime

class TripManager(models.Manager):
    def validate_trip(self, post_data):
        errors = []
        if len(post_data['destination']) < 1:
            errors.append("You must provide a destination.")
        if len(post_data['description']) < 1:
            errors.append("You must provide a description.")
        if len(post_data['trip_start']) < 1:
            errors.append("You must provide a start date.")
        if post_data['trip_start'] < str(datetime.datetime.now()):
            errors.append("You cannot start your trip today or before.")
        if len(post_data['trip_end']) < 1:
            errors.append("You must provide an end date.")
        if post_data['trip_end'] < post_data['trip_start']:
            errors.append("You cannot end your trip before you start it.")
        
        if errors:
            return errors

class Trip(models.Model):
    travelers= []
    destination = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    trip_start = models.CharField(max_length=100)
    trip_end = models.CharField(max_length=100)
    travelers = models.ManyToManyField(User, related_name="trips")
    planner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = TripManager()
    def __str__(self):
        return self.destination