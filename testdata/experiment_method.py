# -*- coding: utf-8 -*-
import codecs,csv,re,math
import numpy as np

#parameter
weight_value = 0.0
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

'''
既存の手法として使用する手法であるコサイン類似度を求める関数たち
'''
#会話内容に基づいたコサイン類似度を出すために使用するデータセット読み込み
#返り値は行が各ユーザ，列が使用した単語の種類と回数
def Reading_dataset():
    f = codecs.open("dataset2.csv","r",encoding="utf-8")
    reader = csv.reader(f)
    csv_data = []
    for i,row in enumerate(reader):
        botname = row[0]
        del row[0]
        csv_data.append(row)
    f.close()
    return csv_data

def cos_sim_matrix(matrix):
    """
    item-feature 行列が与えられた際に
    item 間コサイン類似度行列を求める関数
    """
    d = matrix @ matrix.T  # item-vector 同士の内積を要素とする行列
    # コサイン類似度の分母に入れるための、各 item-vector の大きさの平方根
    norm = (matrix * matrix).sum(axis=1, keepdims=True) ** .5
    # それぞれの item の大きさの平方根で割っている
    return d / norm / norm.T

'''
これより下は提案手法で使用する関数
'''
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
#返り値は{bot1:2,bot2:5,...,}の配列
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

#どのユーザが誰に何回@マークをつけられたか，また誰に@マークを付けるかを配列で返す関数
#引数はCount_replyで作成したカウントの配列
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

#リーダスコアを算出する関数
#引数は引数はCount_replyで作成したカウントの配列と引数はRaeding_csvfileで作成した発言の情報
#細かい内容は関数内のコメント参照
#返り値は各ユーザの水コア
def Leader_score(data_list,data):
    L_score = {}
    for i in data_list:
        L_score[i]=0
    #各ユーザとの会話数の平均が高い人物を出す
    '''
    会話総数/ユーザ数(自身を除く)を出すことで全ユーザでの会話平均数を出す
    ここで平均値が高いユーザ(閾値とかで判定)をリーダ性ありとしてスコアに加算する
    '''
    for user in data_list:
        sum_value = 0
        for value in data_list[user]:
            sum_value += data_list[user][value]
        ave_value = sum_value/(len(data_list)-1)
        #閾値で判定
        if ave_value > L_parameter:
            L_score[user] += 1

    hub_data = Hub(data_list)
    #print(hub_data)

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
            #閾値で判定
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

'''
ランキングスコアのメモ
対象のユーザに対して
α(リーダスコア＋サポートスコア)＋(1-α)会話内容によるコサイン類似度
'''
def ranking(L_result, S_result, cos_result, weight_value):
    usernum = len(L_result)
    a = weight_value
    #ループごとにユーザのスコア算出
    for (i,user) in enumerate(L_result):
        print(user)
        for (j,targetuser) in enumerate(L_result):
            #同じ時はスキップ
            if i == j:
                continue
            score = (a*(L_result[targetuser]+S_result[targetuser][user]))+((1-a)*(cos_result[i][j]))
            print(targetuser,score)

def ranking_log(L_result, S_result, cos_result, weight_value):
    usernum = len(L_result)
    a = weight_value
    print("logあり")
    #ループごとにユーザのスコア算出
    for (i,user) in enumerate(L_result):
        print(user)
        for (j,targetuser) in enumerate(L_result):
            #同じ時はスキップ
            if i == j:
                continue
            sum_score = L_result[targetuser]+S_result[targetuser][user]
            if sum_score == 0:
                score = (a*0)+((1-a)*(cos_result[i][j]))
            else:
                score = (a* math.log(sum_score) )+((1-a)*(cos_result[i][j]))
            print(targetuser,score)

if __name__ == '__main__':
    #データ読み込み
    data = Reading_csvfile()
    
    #コサイン類似度出すまでの一連の処理
    cos_dataset = Reading_dataset()
    cos_data = np.array(cos_dataset)
    cos_data = cos_data.astype(np.int)
    cos_result = cos_sim_matrix(cos_data)
    #print(cos_result[0][0])


    #＠マークのユーザ毎のカウント(例：bot1が誰に何回送ったのか)
    user_rp = Count_reply(data)
    #ユーザが送信したファイルコンテンツ数のカウント
    user_file = Serach_sendfiles(data)

    # ユーザ評価
    L_result = Leader_score(user_rp,data)
    S_result = Support_score(user_rp,user_file)

    print(L_result)
    print(S_result)

    ranking(L_result,S_result,cos_result,weight_value)
    ranking_log(L_result,S_result,cos_result,weight_value)

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

ランキングスコアのメモ
対象のユーザに対して
α(リーダスコア＋サポートスコア)＋(1-α)会話内容によるコサイン類似度

'''