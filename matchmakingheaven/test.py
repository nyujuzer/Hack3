import requests

url = '127.0.0.1:8000'

def makeChallange():
    d = {'matchId':1, 'sender':'gyula', 'recipiant':"pista", 'winner':'none','sender_points':0, 'recipiant_points':0, 'game':'lol', 'map':'summoners brink' }
    response = requests.post('http://127.0.0.1:8000/newChallange/', json=d)
    return response.text
print(makeChallange())
