from rest_framework import serializers
from .models import Spot
class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = ['id', 'occupied', 'owner', 'dateFrom', 'nOfDays']