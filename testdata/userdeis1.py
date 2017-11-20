# -*- coding: utf-8 -*-
#ユーザ距離から知識を育む情報を得られるか出す
import sys,re,codecs,json,os,copy

#どうやってランキング化していくのか
#同じ内容の知識の種類+回数
#例　　　ターゲットA：あ10回、い6回、う8回、え9回、お3回
#       　　　　　B：い7回、え1回、お4回、く7回、ま9回　　　　　スコア12
#                C：あ1回、い8回、う4回、こ8回、な3回　　　　　スコア13
#サポート性、リーダ性のある人物はすべての回数に1.5倍する事

#提案方式である知識における重み付け
#ユーザが現在行っている活動に関する情報の重み付けは未実装(現状Excelで計算)
def distance(user1,user2,index):
    diswight = 0
    #ユーザに対して新たな知識の重み付け
    if index == 1:
        diswight += 1.5
    #サポート性、リーダ性のある人物の重み付け
    if user2 == "bot1" or user2 == "bot2" or user2 == "bot3":
        diswight += 1.5
    else:
        diswight += 1
    return diswight

def notdisrank(t_data,b_data):
    ndisscore = {}
    score = 0
    for name,datavalue in b_data.items():
        for key , value in datavalue.items():
            if key in t_data:
                score += value
        ndisscore[name] = score
        score = 0
    print(ndisscore)
            
def disrank(t_data,b_data):
    disscore = {}
    score = 0
    wordscore = {}
    #人物ごとにループnameでbot名
    for name,datavalue in b_data.items():
        for key , value in datavalue.items():
            #対象ユーザと同じ知識がある場合
            if key in t_data:
                #関数distanceによる重み付け
                value = value * distance(target_name,name,0)
                score += value
                if name not in wordscore:
                    wordscore[name] = []
                wordscore[name].append({key:value})
            #異なる知識情報
            else:
                value = value * distance(target_name,name,1)
                if name not in wordscore:
                    wordscore[name] = []
                wordscore[name].append({key:value})
        disscore[name] = score
        score = 0
    for word in wordscore:
        print(word)
        for w in wordscore[word]:
            print(w)
    print(disscore)
    

if __name__ == '__main__':
    
    #引数の獲得
    target_name = sys.argv[1]
    #ファイル名を名前だけ抜き取る
    filename = os.listdir("bot")

    #botデータの収集
    botdata = {}
    for file in filename:
        name = re.sub(".json","",file)
        f = codecs.open("bot/"+file,"r","utf-8")
        botdata[name] = json.load(f)

    #対象とするユーザのデータ登録
    target_data = copy.deepcopy(botdata[target_name])
    #対象のユーザだけ削除
    del botdata[target_name]
    
    disrank(target_data,botdata)
    notdisrank(target_data,botdata)

