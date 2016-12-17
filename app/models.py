from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Players(models.Model):
    user = models.OneToOneField(User, default = None)
    red = models.IntegerField()
    blue = models.IntegerField()
    yellow = models.IntegerField()
    green = models.IntegerField()
    hp = models.IntegerField()
    status = models.IntegerField()
    
class Teams(models.Model):
    name = models.CharField(max_length = 20)
    num_of_member = models.IntegerField()
    player = models.ManyToManyField(Players)
    
class Games(models.Model):
    timestamp = models.DateTimeField(default = timezone.now, db_index = True)
    team = models.ManyToManyField(Teams)
    


