# -*- coding: utf-8 -*-
import codecs,csv,re

#parameter
L_parameter = 4
S_parameter = 4

#csvデータを読み込む関数
#返り値はbot1{{time:ti,text:""},...,}の配列になる
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

#各ユーザが送ったリプライをカウントする関数
#引数はRaeding_csvfileで作成した発言の情報
#返り値はbot1{bot2:3,bot3:...,},...,の送った回数の配列
def Count_reply(data_list):
    repget = " @\S+"
    users_reply = {}
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
        users_reply[user] = user_count
    return users_reply

#ファイルをアップロードしたユーザのカウントを行う関数
#引数はRaeding_csvfileで作成した発言の情報
#返り値は
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

def Hub(data_list):
    hub = {}
    for user in data_list:
        hub[user] = {"resive":{},"send":{}}

    for user in data_list:
        resive = {"bot1":0,"bot2":0,"bot3":0,"bot4":0,"bot5":0,"bot6":0,"bot7":0}
        #print(user,data_list[user])
        #resiveのカウント
        for o_user in data_list:
            for key in data_list[o_user]:
                #print(data_list[o_user][data])
                if user == key :
                    resive[o_user] += data_list[o_user][key]
        del resive[user]
        hub[user]["resive"] = resive 
        hub[user]["send"] = data_list[user]
    return hub




#関数の機能と必要な引数＋返り値に何が来るのか書くこと
def Leader_score(data_list,data):
    L_score = {}
    for i in data_list:
        L_score[i]=0
    #各ユーザとの会話数の平均が高い人物を出す
    for user in data_list:
        sum_value = 0
        for value in data_list[user]:
            sum_value += data_list[user][value]
        ave_value = sum_value/len(data_list)
        if ave_value > L_parameter:
            L_score[user] += 1

    hub_data = Hub(data_list)

    #会話のスタートに立つ人物
    tgget = "#start"
    start_count = {}
    for user in data:
        count = 0
        for session in data[user]:
            matchtext = re.finditer(tgget,session["text"])
            for match in matchtext:
                count += 1
        start_count[user] = count
        L_score[user] += count  
    #指示を促す指示の内容
    odget = "#order"
    order_count = {}
    for user in data:
        count = 0
        for session in data[user]:
            matchtext = re.finditer(odget,session["text"])
            for match in matchtext:
                count += 1
        order_count[user] = count
        L_score[user] += count
    return L_score

def Support_score(data_list,file_list):
    S_score = {}
    #他ユーザの会話数合計が多い人物
    for user in data_list:
        user_count = {"bot1":0,"bot2":0,"bot3":0,"bot4":0,"bot5":0,"bot6":0,"bot7":0}
        for count in data_list[user]:
            if data_list[user][count] > S_parameter:
                user_count[count] += 1
        del user_count[user]
        S_score[user] = user_count
    #他者が必要とする情報や資料を提供する
    '''今回は手動(ファイルを渡した相手(＠した人)に対してスコアを加点するように作成する)
    for user in file_list:
        print(user,file_list[user])
    '''
    S_score["bot2"]["bot4"] += 1
    S_score["bot2"]["bot5"] += 1
    S_score["bot2"]["bot6"] += 1
    S_score["bot2"]["bot7"] += 1
    S_score["bot2"]["bot6"] += 1
    S_score["bot2"]["bot7"] += 1    
    S_score["bot2"]["bot7"] += 1
    S_score["bot2"]["bot4"] += 1
    S_score["bot2"]["bot5"] += 1
    S_score["bot2"]["bot6"] += 1
    S_score["bot2"]["bot7"] += 1
    return S_score

if __name__ == '__main__':
    #データ読み込み
    data = Reading_csvfile()
    
    #＠マークのユーザ毎のカウント(例：bot1が誰に何回送ったのか)
    user_rp = Count_reply(data)
    #ユーザが送信したファイルコンテンツ数のカウント
    user_file = Serach_sendfiles(data)

    # ユーザ評価
    L_result = Leader_score(user_rp,data)
    S_result = Support_score(user_rp,user_file)

    print(user_file)
    '''
    #結果の表示
    sorted(L_result.items(), key=lambda x: -x[1])
    print("リーダ性")
    for i in L_result:
        print(i,L_result[i])

    print("サポート性")
    for i in S_result:
        print(i,"が持つ各ユーザに対してのサポート性")
        i_re = sorted(S_result[i].items(),key=lambda x: -x[1])
        for j in i_re:
            if j[1] == 0:
                continue
            print(j[0],j[1])
    '''

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

それぞれのスコア表を作る
リーダ性　bot1:100,bot2:89,...とか
サポート性 bot1:{bot2:30,bot3:89,...},bot2:{bot1:54,....},....かな
'''