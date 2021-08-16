from django.db import models


# Create your models here.
class Room(models.Model):
  code = models.CharField(max_length=8, default="", unique=True)
  host = models.CharField(max_length=50, unique=True)
  can_guest_pause = models.BooleanField(default=False)
  votes_to_skip = models.IntegerField(default=1)
  create_at = models.DateTimeField(auto_now_add=True)