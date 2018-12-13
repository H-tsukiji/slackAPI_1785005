# -*- coding: utf-8 -*-
#ユーザが指定したリプライ(＠マークのやつ)のカウントを行うプログラム
import sys,re,codecs,json,os,glob,csv

files = []
files = glob.glob('20180925/*.txt')

fm = codecs.open("memberlist.json","r","utf-8")
memberlist = json.load(fm)

def search_nameindex(username):
    for i in memberlist:
        if (username in i["id"]) == True:
            name = i["name"]
    return name

#1行づつ読み込みノイズとなるような記号とひらがなを排除
def cleanInput(text):
    text = re.sub('@', '', text)
    text = re.sub('<', '', text)
    text = re.sub('>', '', text)
    text = search_nameindex(text)
    return text

if __name__ == '__main__':

    for inputfile in files:

        #ファイル読み込み
        file = open(inputfile, 'r', encoding="utf-8")
        fline = file.readlines()
        file.close()
        #ファイル名を名前だけ抜き取る
        username = os.path.basename(inputfile)
        username = re.sub("\.txt","",username)

        re_index = {}
        for line in fline:
            #ユーザ指定のタグを検知する正規表現<@U0JACJLRJ>や<@U0J8PMAQJ|t.kasai>
            reget = "<@\S{9}>"
            matchtext = re.finditer(reget,line)
            if matchtext:
                for result in matchtext:
                    key = result.group()
                    if (key in re_index) == False:
                        re_index[key] = 1
                    else:
                        re_index[key] = re_index[key] + 1

        re_index = sorted(re_index.items(), key=lambda x:x[1],reverse=True)

        try:
            with open("rep_"+username+".csv", 'w', encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile, lineterminator='\n')
                writer.writerow(['userid', 'count'])
                for i in re_index:
                    writer.writerow([cleanInput(i[0]),i[1]])
        # 起こりそうな例外をキャッチ
        except FileNotFoundError as e:
            print(e)
        except csv.Error as e:
            print(e)