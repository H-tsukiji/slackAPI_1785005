# -*- coding: utf-8 -*-
#ログjsonファイルからslackのリアクションを取る
#取る物
# リアクションをもらった文面
# 貰った相手の情報
# 誰からもらったのか

import codecs,json,csv,glob
from datetime import datetime

#フォルダjson内にあるすべてのjsonファイルを取得する。
files = []
files = glob.glob('../json/20180925/*.json')

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
    for i in logfile:
        if 'reactions' in i:
            #print(i['reactions'][0])
            count = i['reactions'][0]['count']
            name = search_nameindex(i['user'])
            for j in logs:
                if name == j['name']:
                    j['count'] += count

if __name__ == '__main__':
    
    user_reactions = []

    for name in memberlist:
        user_reactions.append({'name':name['name'],'count':0})
    
    for f in files:
        # ログのJSONファイルの読み込み
        fl = codecs.open(f, "r", "utf-8")
        f_json = json.load(fl)
        loggets(f_json['messages'],user_reactions)

    
    try:
        with open('count_reaction.csv', 'w', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, lineterminator='\n')
            writer.writerow(['user', 'count'])
            for i in user_reactions:
                writer.writerow([i['name'], i['count']])
    # 起こりそうな例外をキャッチ
    except FileNotFoundError as e:
        print(e)
    except csv.Error as e:
        print(e)
    
    #print(user_reactions)
