# -*- coding: utf-8 -*-
#APIを使って対象のチャンネルのログをjson形式で取得するプログラム
import sys,codecs,json,glob,csv
from slacker import Slacker

# API token tokenが入ったファイルの読み込みをして取得(セキュリティ回避)
token = codecs.open("../../slackapi_token.txt", "r","utf-8")
slacker = Slacker(token)

#フォルダjson内にあるすべてのjsonファイルを取得する。
files = []
files = glob.glob('../json/20180925/*.json')

fm = codecs.open("memberlist.json","r","utf-8")
memberlist = json.load(fm)

#ユーザidとユーザ名の紐付け
def search_nameindex(username):
    global name
    for i in memberlist:
        if (username in i["id"]) == True:
            name = i["name"]
    return name

'''
#やっぱ使わない
def get_threadtl(c_name,thread_ts):
    result = slacker.channels.replies(c_name, thread_ts).body
    #JSON形式に変換しファイルに出力
    f = codecs.open("ore.json","w","utf-8")
    f.write(json.dumps(result,indent=3,ensure_ascii=False));
    f.close()
'''

def start_thread(file_list, first_thread,thread_count):
    for log in file_list:
        if ("thread_ts" in log) and ("replies" in log):
            first_name = search_nameindex(log['user'])
            for i in first_thread:
                if first_name == i['name']:
                    i['count'] += 1
            for i in thread_count:
                if first_name == i['name']:
                    i['count'] += 1
            for j in log["replies"]:
                rep_name = search_nameindex(j['user'])
                for i in thread_count:
                    if rep_name == i['name']:
                        i['count'] += 1

if __name__ == "__main__":

    first_thread = []
    thread_count = []
    for user in memberlist:
        first_thread.append({'name':user['name'],'count':0})
        thread_count.append({'name':user['name'],'count':0})

    for f in files:
        # ログのJSONファイルの読み込み
        fl = codecs.open(f, "r", "utf-8")
        f_json = json.load(fl)
        start_thread(f_json['messages'], first_thread,thread_count)
    #print(first_thread)
    #print(thread_count)

    '''
    c_name = "C4W2RL2BA"
    thread_ts = "1535352566.000100"
    get_threadtl(c_name, thread_ts)
    '''

    #スレッドの初めとなった回数をcsvで出力
    try:
        with open('first_thread_user.csv', 'w', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, lineterminator='\n')
            writer.writerow(['user', 'first_thread_count'])
            for i in first_thread:
                writer.writerow([i['name'], i['count']])
    # 起こりそうな例外をキャッチ
    except FileNotFoundError as e:
        print(e)
    except csv.Error as e:
        print(e)

    #スレッド内の会話回数を各ユーザ毎にcsvで出力
    try:
        with open('thread_message_countlist.csv', 'w', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, lineterminator='\n')
            writer.writerow(['user', 'message_count'])
            for i in thread_count:
                writer.writerow([i['name'], i['count']])
    # 起こりそうな例外をキャッチ
    except FileNotFoundError as e:
        print(e)
    except csv.Error as e:
        print(e)
