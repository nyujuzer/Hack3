from django.http import JsonResponse
from .models import Spot
from .serializers import SpotSerializer
def allSpots(request):
    spots = Spot.objects.all()
    serializer = SpotSerializer(spots, many=True)
    return JsonResponse({"AvailableSpots":serializer.data}, safe=False)