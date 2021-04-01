import requests
import json


def searchQ(query):
    searchUrl = "https://en.wikipedia.org/w/api.php?action=opensearch&limit=10&namespace=0&format=json&search="
    try:
        respon = requests.request("GET", searchUrl+query)
    except requests.exceptions.RequestException as e:
        print(e)
    return json.loads(respon.content)
