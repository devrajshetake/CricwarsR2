from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class GroupR2(models.Model):
    name = models.CharField(max_length=100, default="")
    total_users = models.IntegerField(default=6)

    def getPlayers(self):
        queryset = self.players.all()
        return queryset

    def getResponses(self):
        queryset = self.responses.all()

    def setPlayerRating(self):
        responses = getResponses()
        for res in responses:
            res.player.rating += (res.rating/self.total_users)
            res.player.save()

    def __str__(self):
        return self.name

class User(AbstractUser):
    groupr2 = models.ForeignKey(GroupR2, on_delete = models.CASCADE, null = True, blank = True, related_name="grpusers")
    canAccessFinalRatings = models.BooleanField(default=False)
    canSelectTeam = models.BooleanField(default=False)
    canRatePlayers = models.BooleanField(default=True)

    def __str__(self):
        return self.username

class Team(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, blank=True,related_name="teams")
    total_score = models.FloatField(default=0)
    def __str__(self):
        return f"{self.user.username} : {self.user.groupr2}"

    def getPlayers(self):
        print(self.teamplayers.all())
        return self.teamplayers.all()

class Player(models.Model):
    name = models.CharField(max_length=100, default="")
    price = models.FloatField(default=0)
    rating = models.FloatField(default=0)
    final_rating = models.FloatField(default=0)
    role = models.CharField(max_length=50)
    dr = models.FloatField(default=0, verbose_name = "Conditional Rating Change")
    groupr2 = models.ForeignKey(GroupR2, on_delete = models.PROTECT, null = True, blank = True, related_name="players")
    img = models.URLField(blank=True, default="https://drive.google.com/uc?export=view&id=1f_Hr2NYr2XrecCxmIK23fNCLjsJo-ReQ")
    teams = models.ManyToManyField(Team, related_name="teamplayers")

    def __str__(self):
        return self.name
    

class PlayerResponse(models.Model):
    player = models.ForeignKey(Player, on_delete = models.CASCADE, related_name="playerResponses")
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return f'{self.player} : {self.rating}'





