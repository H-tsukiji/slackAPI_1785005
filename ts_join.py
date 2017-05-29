# -*- coding: utf-8 -*-

import codecs, json, datetime
#ログのJSONファイルの読み込み
f = codecs.open("slack_C0J8KM6KF.json","r","utf-8")
f1 = json.load(f)
f = codecs.open("slack_C0XMH9F0Q.json","r","utf-8")
f2 = json.load(f)
f = codecs.open("slack_C4W2RL2BA.json","r","utf-8")
f3 = json.load(f)
f = codecs.open("slack_C18JT8ZNY.json","r","utf-8")
f4 = json.load(f)
fm = codecs.open("memberlist.json","r","utf-8")
memberlist = json.load(fm)

month = []

for i in f1["messages"]:
    d = datetime.datetime.fromtimestamp(float(i["ts"]))
    for j in range(12):
        if d.month == j+1:
            month.append({int(j+1):{"user": i["user"], "text": i["text"], "date": d, "ts": i["ts"], "channel": "f1"}})

for i in f2["messages"]:
    d = datetime.datetime.fromtimestamp(float(i["ts"]))
    for j in range(12):
        if d.month == j+1:
            month.append({int(j+1):{"user": i["user"], "text": i["text"], "date": d, "ts": i["ts"], "channel": "f2"}})

for i in f3["messages"]:
    d = datetime.datetime.fromtimestamp(float(i["ts"]))
    for j in range(12):
        if d.month == j+1:
            month.append({int(j+1):{"user": i["user"], "text": i["text"], "date": d, "ts": i["ts"], "channel": "f3"}})

for i in f4["messages"]:
    if (i.get("subtype") == "file_comment"):
        continue
    d = datetime.datetime.fromtimestamp(float(i["ts"]))
    for j in range(12):
        if d.month == j+1:
            month.append({int(j+1):{"user": i["user"], "text": i["text"], "date": d, "ts": i["ts"], "channel": "f4"}})


def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown type")

#JSON形式に変換しファイルに出力
f = codecs.open("test.json","w","utf-8")
f.write(json.dumps(month, default=datetime_handler));
f.close()
