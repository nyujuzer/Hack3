import json
import requests
def main():
    data = "MOCK_DATA.json"

    domain = "127.0.0.1:8000/"
    url = "put/"

    x=0
    with open(data) as f:
        for i in f:
            x+=1
            if "true" in i:
                i.replace("true", "True")
            elif "false" in i:
                i.replace("false","False")
            j = json.loads(i)
            print(x)
            requests.post("http://127.0.0.1:8000/put/", json=j)

