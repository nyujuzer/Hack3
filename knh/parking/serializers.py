from rest_framework import serializers
from . import models
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.user
        fields = ['id','name','password','games', 'friends']

class gameSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = models.game
        fields = ['gameName', 'genre', 'elo', 'hasWon']
class chalangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.challange
        fields = ['challangeId','sender','recipient','playedGame']
class teamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.team
        fields = ['tempId', 'avarageElo', 'memeberIds']