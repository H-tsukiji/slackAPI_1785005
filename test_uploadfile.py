import requests

with open("id_and_pw2017.pdf",'rb') as f:
    param = {'token': "xoxp-18292672947-18354986291-166689903238-d1ff9554866a15e73129eb85d808d055" ,
            'channels': "@tsukiji",
            'title': "ファイル" }
    r = requests.post("https://slack.com/api/files.upload", params=param,files={'file':f})
    print (r.text)

