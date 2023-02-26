from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from os import path
from random import randint as rnd 
from matchmakingheaven.settings import BASE_DIR
from.models import Tournament, match
from .serializers import matchSerializer
from rest_framework.decorators import api_view
import json

def login(request, userName, password): 
    print(BASE_DIR)
    f = open(path.join(BASE_DIR, 'data/user.json'), )
    x = json.loads(f.read())
    if userName == x['username'] and x[password] == password:
        return JsonResponse(x)
    else:
        return JsonResponse({"response":"failed, due to incorrect password"})

@api_view(['POST'])
def makeChallange(request):
    matchId = rnd(1000,9999)
    #y = list(map(lambda x : "'"+x+"'",[sender, recipiant, 0, game, _map,]))
    #x = 'matchId:'+y[0]+', sender:'+y[1]+', recipiant:'+y[2]+',sender_points:'+y[3]+', recipiant_points:'+y[3]+', game:'+y[4]+', map:'+y[5]
    print(request.data)
    serializer = matchSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'data':serializer.data['matchId']})
    else:
        return JsonResponse({"success":False})
    
@api_view(['GET'])
def getNames(request, id, spoints, rpoints):
    mog = match.objects.get(pk=id)
    mog.sender_points = spoints
    mog.recipiant_points = rpoints
    if spoints > rpoints:
        mog.winner = mog.sender
    elif spoints < rpoints:
        mog.winner = mog.recipiant
    else:
        mog.winner = "tie"
    
    mog.save()

    print("good")
    return JsonResponse({'sender':mog.sender, 'recipiant':mog.recipiant})
    
        #return JsonResponse({'success':False})