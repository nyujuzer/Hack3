from django.db import models

matchCount = 0
class match(models.Model):
    matchId = models.IntegerField(primary_key=True)
    sender = models.CharField(max_length=255)
    recipiant = models.CharField(max_length=255)
    winner = models.CharField(max_length=255)
    sender_points = models.IntegerField()
    recipiant_points = models.IntegerField()
    game = models.CharField(max_length=255)
    map = models.CharField(max_length=255)
class Tournament(models.Model):
    tournamentId = models.IntegerField(primary_key=True)
    matchIds = models.CharField(max_length=255)
