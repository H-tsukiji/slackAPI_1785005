# -*- coding: utf-8 -*-
#ログjsonファイルからslackのリアクションしてもらった人物とそのされた回数を出力するプログラム
#取る物(まだ)
# リアクションをもらった文面
# 誰からもらったのか
# それに加えてリアクションした人の一覧とその回数

import codecs,json,csv,glob,re
from datetime import datetime

#フォルダjson内にあるすべてのjsonファイルを取得する。
files = []
files = glob.glob('../json/20180925/*.json')

fm = codecs.open("memberlist.json","r","utf-8")
memberlist = json.load(fm)

def search_nameindex(username):
    for i in memberlist:
        if (username in i["id"]) == True:
            name = i["name"]
    return name

#他ユーザからリアクションを受けた回数を辞書に記録する関数    
def count_reactions(logfile, list_users):
    for i in logfile:
        if 'reactions' in i:
            count = 0
            for reaction in i['reactions']:
                count += reaction['count']
                name = search_nameindex(i['user'])
                for j in list_users:
                    if name == j['name']:
                        j['count'] += count

def Reactioners(logfile, reaction_list):
    for i in logfile:
        if 'reactions' in i:
            count = 0
            touser = search_nameindex(i['user'])
            for reaction in i['reactions']:
                for user in reaction['users']:
                    name = search_nameindex(user)
                    text = cleanInput(i['text'])
                    reaction_list.append({"user":name, "touser":touser , "text":text})

#1行づつ読み込みノイズとなるような記号とひらがなを排除
def cleanInput(text):
    text = re.sub('\n', ' ', text)
    text = re.sub('\r\n', ' ', text)
    return text


if __name__ == '__main__':
    
    list_users = []
    reaction_list = []

    for name in memberlist:
        list_users.append({'name':name['name'],'count':0})
    
    for f in files:
        # ログのJSONファイルの読み込み
        fl = codecs.open(f, "r", "utf-8")
        f_json = json.load(fl)
        count_reactions(f_json['messages'],list_users)
        Reactioners(f_json['messages'],reaction_list)

    #print(list_users)
    #print(reaction_list)

    
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

    try:
        with open('reaction_list.csv', 'w', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, lineterminator='\n')
            writer.writerow(['user', 'touser', 'text'])
            for i in reaction_list:
                writer.writerow([i['user'], i['touser'], i['text']])
    # 起こりそうな例外をキャッチ
    except FileNotFoundError as e:
        print(e)
    except csv.Error as e:
        print(e)