from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class WatchList(models.Model):
    title = models.CharField(max_length=80)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ListEntry(models.Model):
    title = models.CharField(max_length=255)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE)
    seen = models.BooleanField(default=False)
    isfavourite = models.BooleanField(default=False)
