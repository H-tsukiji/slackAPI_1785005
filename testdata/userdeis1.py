# -*- coding: utf-8 -*-
#ユーザ距離から知識を育む情報を得られるか出す
import sys,re,codecs,json,os,copy

#どうやってランキング化していくのか
#同じ内容の知識の種類+回数
#例　　　ターゲットA：あ10回、い6回、う8回、え9回、お3回
#       　　　　　B：い7回、え1回、お4回、く7回、ま9回　　　　　スコア12
#                C：あ1回、い8回、う4回、こ8回、な3回　　　　　スコア13
#サポート性、リーダ性のある人物はすべての回数に1.5倍する事

def distance():
    pass

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

    #人物ごとにループnameでbot名
    for name,datavalue in b_data.items():
        for key , value in datavalue.items():
            if key in t_data:
                #リーダ性、サポート性の重み付け
                '''
                サポート性の重み付けの値を入れておく辞書を作成する。
                {bot1:{bot2:1.8,}}

                '''
                if name == "bot1" or name == "bot2" or name == "bot3":
                    value = value * 1.5
                    score += value
                #ここにリーダ性の重み付けする
                if name == "bot1" or name == "bot2" or name == "bot3":
                    pass
                else:
                    score += value
        disscore[name] = score
        score = 0
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
