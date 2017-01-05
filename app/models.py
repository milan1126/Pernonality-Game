from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PlayerManager(models.Manager):
    def create_player(self, user, red=0, blue=0, yellow=0, green=0, hp=100, status=0):
        player = self.create(user=user, red=red, blue=blue, yellow=yellow, green=green, hp=hp, status=status)
        return player

class Players(models.Model):
    user = models.OneToOneField(User, default = None)
    red = models.IntegerField()
    blue = models.IntegerField()
    yellow = models.IntegerField()
    green = models.IntegerField()
    hp = models.IntegerField()
    status = models.IntegerField()
    
    objects = PlayerManager()
    
class Teams(models.Model):
    name = models.CharField(max_length = 20)
    num_of_member = models.IntegerField()
    player = models.ManyToManyField(Players)
    
class Games(models.Model):
    timestamp = models.DateTimeField(default = timezone.now, db_index = True)
    team = models.ManyToManyField(Teams)
    


