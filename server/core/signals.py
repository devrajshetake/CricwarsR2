from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=PlayerResponse)
def update_rating(sender, instance, created, **kwargs):
    if created:
        player = instance.player
        player.final_rating += instance.rating / player.groupr2.total_users
        player.save()

@receiver(post_save, sender=User)
def create_team(sender, instance, created, **kwargs):
    if created:
        Team.objects.create(user=instance)

@receiver(post_save, sender=Team)
def compute_score(sender, instance, created, **kwargs):
    players = instance.getPlayers()
    score = 0
    for player in players:
        score += (player.final_rating + player.dr)
    # cant use save as recursion
    user = instance.user
    print(score, "called")
    print(user)

    user.score = score
    user.save()
    Team.objects.filter(id=instance.id).update(total_score=round(score,2))