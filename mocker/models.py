from django.db import models


# Create your models here.
class Users(models.Model):
    username = models.CharField(null=False, blank=False, max_length=100)


class Clicks(models.Model):
    TYPES = [
        (1, 'fat'),
        (2, 'stupid'),
        (3, 'dumb'),
    ]
    type = models.IntegerField(choices=TYPES, blank=False, default=1)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=False)
    count = models.IntegerField(blank=True, null=True, default=0)
