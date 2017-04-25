import requests
import codecs

token = codecs.open("..\slackapi_token.txt","r","utf-8")

with open("id_and_pw2017.pdf",'rb') as f:
    param = {'token': token ,
            'channels': "@tsukiji",
            'title': "ファイル" }
    r = requests.post("https://slack.com/api/files.upload", params=param,files={'file':f})
    print (r.text)

