import requests
import json


def getLeetToken(language, code, inputText):
    url = "https://leetcode.com/playground/api/runcode"
    body = {"lang": language, "typed_code": code, "data_input": inputText}
    headers = {"Content-Type": "application/json"}
    r = requests.post(url, data=json.dumps(body), headers=headers)
    return r.json()


def checkLeetStatus(token):
    url = "https://leetcode.com/submissions/detail/"+token+"/check/"
    r = requests.get(url)

    return r.json()
