# -*- coding: utf-8 -*-

import codecs,json,csv
from datetime import datetime
#ログのJSONファイルの読み込み
f = codecs.open("slack_C0XMH9F0Q.json","r","utf-8")
f_json = json.load(f)
fm = codecs.open("memberlist.json","r","utf-8")
memberlist = json.load(fm)



"""
#隔離
#まずはf_json["messages"][番号]["user"]でユーザ名
#具体例：i={'type': 'message', 'text': '教員の押印が必要なので、私にも簡単に報告するようにお願いします。', 'user': 'U0JACJLRJ', 'ts': '1493299059.166830'}
for i in f_json["messages"]:
    if (i["user"] in index_username)  == False :
        index_username.append(i["user"])
    else:
        count += 1

print(index_username)
"""

#csvファイルに発言、時間、人のデータを書き込む
#member.jsonでユーザ名に変換

try:
    # 書き込み UTF-8
    with open('log_grad2017_channel.csv', 'w', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, lineterminator='\n')
        writer.writerow(['User', 'text', 'time'])
        for i in f_json["messages"]:
            for j in memberlist :
                if(i.get("subtype") == "file_comment"):
                    continue
                if(i['user'] in j["id"]) == True :
                    username = j["name"]
            writer.writerow([username, i["text"], float(i["ts"]), datetime.fromtimestamp(float(i["ts"]))])

# 起こりそうな例外をキャッチ
except FileNotFoundError as e:
    print(e)
except csv.Error as e:
    print(e)

