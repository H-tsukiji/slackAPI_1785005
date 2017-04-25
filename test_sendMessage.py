import requests

payload ={
    "token" : "xoxp-18292672947-18354986291-166689903238-d1ff9554866a15e73129eb85d808d055",
    "channel" : "@tsukiji",
    "text" : "Hello",
    "username": "mybot",
    "pretty" : "1"
}

url = "https://slack.com/api/chat.postMessage"

res = requests.post(url, params=payload)

print (res.text)