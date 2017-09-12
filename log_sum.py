# -*- coding: utf-8 -*-
#各チャンネルのログを統合し、まとめたログの作成
import codecs,json,csv,glob
from datetime import datetime

#フォルダcsv内にあるすべてのcsvファイルを取得する。
files = []
files = glob.glob('json\*.json')

fm = codecs.open("memberlist.json","r","utf-8")
memberlist = json.load(fm)

sumlog = []

#csvファイルに発言、時間、人のデータを書き込む
#member.jsonでユーザ名に変換
for f in files:
    # ログのJSONファイルの読み込み
    fl = codecs.open(f, "r", "utf-8")
    f_json = json.load(fl)
    try:
        for i in f_json["messages"]:
            for j in memberlist:
                if (i.get("subtype") == "file_comment"):
                    continue
                if (i['user'] in j["id"]) == True:
                    username = j["name"]
            sumlog.append([username, i["text"], float(i["ts"]), datetime.fromtimestamp(float(i["ts"]))])
    # 起こりそうな例外をキャッチ
    except FileNotFoundError as e:
        print(e)

sumlog = sorted(sumlog, key=lambda x:(x[0],x[2]))

with open('slacklog.csv', 'a', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, lineterminator='\n')
    writer.writerow(['User', 'text', 'timestamp', 'time'])
    for i in sumlog:
        writer.writerow([i[0], i[1], i[2], i[3]])

