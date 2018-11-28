# -*- coding: utf-8 -*-
#ログjsonファイルからslackのリアクションしてもらった人物とそのされた回数を出力するプログラム


#取る物(まだ)
# リアクションをもらった文面
# 誰からもらったのか
# それに加えてリアクションした人の一覧とその回数


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

def count_reactions(logfile, list_users):
    for i in logfile:
        if 'reactions' in i:
            #print(i['reactions'][0])
            count = i['reactions'][0]['count']
            name = search_nameindex(i['user'])
            for j in list_users:
                if name == j['name']:
                    j['count'] += count

if __name__ == '__main__':
    
    list_users = []

    for name in memberlist:
        list_users.append({'name':name['name'],'count':0})
    
    for f in files:
        # ログのJSONファイルの読み込み
        fl = codecs.open(f, "r", "utf-8")
        f_json = json.load(fl)
        count_reactions(f_json['messages'],list_users)

    
    try:
        with open('count_reaction.csv', 'w', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, lineterminator='\n')
            writer.writerow(['user', 'count'])
            for i in list_users:
                writer.writerow([i['name'], i['count']])
    # 起こりそうな例外をキャッチ
    except FileNotFoundError as e:
        print(e)
    except csv.Error as e:
        print(e)
    
    #print(list_users)
