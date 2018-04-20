# -*- coding: utf-8 -*-
#ログjsonファイルからslackのリアクションを取る
#取る物
# リアクションをもらった文面
# 貰った相手の情報
# 誰からもらったのか

import codecs,json,csv
from datetime import datetime

#ログのJSONファイルの読み込み
# 対象のチャンネル名
# general:C0J8KM6KF  seminar1421:C18JT8ZNY  report:C0XMH9F0Q  grad2017:C4W2RL2BA  chat:C0J8Q0DK9
f = codecs.open("../json/20180419/slack_C4W2RL2BA.json","r","utf-8")
f_json = json.load(f)
fm = codecs.open("memberlist.json","r","utf-8")
memberlist = json.load(fm)

def append_index(index, username, text, ts, date_ts):
    index.append([username, text, ts, date_ts])

def search_nameindex(username):
    for i in memberlist:
        if (username in i["id"]) == True:
            name = i["name"]
    return name

def loggets(logfile, logs):
    try:
        for i in logfile:
            if ('user' in i ) and ( 'text' in i ):
                name = search_nameindex(i['user'])
                append_index(logs, name, i['text'], float(i['ts']), datetime.fromtimestamp(float(i["ts"])))
                continue

            elif ('user' not in i ) or ('text' not in i):
                if 'bot_id' in i: 
                    append_index(logs, i['bot_id'], i['text'], float(i['ts']), datetime.fromtimestamp(float(i["ts"])))         
                    continue

                if 'comment' in i:
                    name = search_nameindex(i['comment']['user'])
                    #print(i['comment']['user'], i['comment']['comment'], i['comment']['timestamp'])
                    append_index(logs, name, i['comment']['comment'], float(i['comment']['timestamp']), datetime.fromtimestamp(float(i['comment']['timestamp'])))
                    continue
    # 起こりそうな例外をキャッチ
    except FileNotFoundError as e:
        print(e)


if __name__ == '__main__':
    

    pass