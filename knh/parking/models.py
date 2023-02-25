from django.db import models

class user(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    games = models.CharField(max_length=255)
    friends = models.CharField(max_length=255)
    matches = models.IntegerField()


class game(models.Model):
    gameName = models.CharField(max_length=255, primary_key=True)
    genre = models.CharField(max_length=255)
    elo = models.IntegerField()
    hasWon = models.BooleanField()

class interaction(models.Model):
    challange = models.BooleanField()
    team = models.BooleanField()

class challange(models.Model):
    sender = models.IntegerField()
    recipient = models.IntegerField()
    challangeid = models.IntegerField(primary_key=True)
    playedGame = models.CharField(max_length=255)  
    winner = models.CharField(max_length=255, blank=True)

class team(models.Model):
    tempId = models.IntegerField(primary_key=True)
    avarageElo = models.IntegerField()
    memeberIds = models.CharField(max_length=255)