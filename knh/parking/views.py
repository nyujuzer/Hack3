from django.http import JsonResponse
from .models import Spot
from .serializers import SpotSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET'])
def allSpots(request):
    spots = Spot.objects.all().filter(occupied=False)
    serializer = SpotSerializer(spots, many=True)
    
    return JsonResponse({"AvailableSpots":serializer.data}) 

@api_view(['POST'])
def Fill(request):
    serializer = SpotSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

