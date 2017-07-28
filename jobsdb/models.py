from __future__ import unicode_literals

from django.db import models



class Location(models.Model):
    location_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.location_name
   
class Connection(models.Model):
    location = models.ForeignKey(Location)
    ip = models.CharField(max_length=200)
    port = models.IntegerField(default=0)
    mfdbname= models.CharField(max_length=200)
    bfdbname= models.CharField(max_length=200)

    def __str__(self):
        return self.ip
