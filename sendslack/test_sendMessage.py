import requests
import codecs

token = codecs.open("../slackapi_token.txt", "r","utf-8")

payload ={
    "token" : token,
    "channel" : "@tsukiji",
    "text" : "Hello",
    "username": "mybot",
    "pretty" : "1"
}

url = "https://slack.com/api/chat.postMessage"

res = requests.post(url, params=payload)

print (res.text)