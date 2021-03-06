from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Television(models.Model):
    name = models.CharField(max_length=200)
    time = models.TimeField()
    description = models.TextField()
    date = models.DateField()
    isAd = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def publish(self):
        self.date
        self.save()