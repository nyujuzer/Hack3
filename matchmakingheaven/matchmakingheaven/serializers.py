from rest_framework import serializers
from .models import match, Tournament
class matchSerializer(serializers.ModelSerializer):
    class Meta:
        model = match
        fields = ['matchId', 'sender', 'recipiant', 'winner', 'sender_points', 'recipiant_points', 'game','map']