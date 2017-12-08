# -*- coding: utf-8 -*-
import codecs,csv,re

def Reading_csvfile():
    f = codecs.open("sessiondata.csv","r",encoding="utf-8")
    reader = csv.reader(f)
    header = next(reader)
    csv_data = {}
    for row in reader:
        if (row[0] not in csv_data) == True :
            csv_data[row[0]] = []
        csv_data[row[0]].append({"time":row[1],"text":row[2]})
    f.close()
    return csv_data

def Count_repray(data_list):
    repget = " @\S+"
    users_repray = {}
    for user in data_list:
        count = 0
        user_count = {"bot1":0,"bot2":0,"bot3":0,"bot4":0,"bot5":0,"bot6":0,"bot7":0}
        for session in data_list[user]:
            matchtext = re.finditer(repget,session["text"])
            for match in matchtext:
                key = str(match.group()).replace(" @","")
                user_count[key] += 1
                count += 1
        del user_count[user]
        users_repray[user] = user_count
    return users_repray

def Serach_sendfiles(data_list):
    fget = "<file upload>"
    users_contents = {}
    for user in data_list:
        count = 0
        for session in data_list[user]:
            matchtext = re.finditer(fget,session["text"])
            for match in matchtext:
                count += 1
        users_contents[user] = count
    return users_contents

if __name__ == '__main__':
    #データ読み込み
    data = Reading_csvfile()
    #＠マークのユーザ毎のカウント(例：bot1が誰に何回送ったのか)
    user_rp = Count_repray(data)
    #ユーザが送信したファイルコンテンツ数のカウント
    user_file = Serach_sendfiles(data)
    print(user_file)
    print(user_rp)

    # ユーザ評価
    #各ユーザとの会話数の平均が高い人物を出す
    #他ユーザの会話数合計が多い人物
    #一人当たりの会話数の総数が一定数以上である


'''
リーダ性を持つ人物
・指示を促す指示の内容
・会話のスタートに立つ人物
・各ユーザとの会話数の平均が高い人物


サポート性を持つ人物の定義
・他者からの問いかけに対して反応が早い
・他ユーザの会話数合計が多い人物
    一人当たりの会話数の総数が一定数以上である
・他者が必要とする情報や資料を提供する
・これらの特徴毎にスコアを加算してくことで一定以上の値に達する人物に対してサポート性
'''