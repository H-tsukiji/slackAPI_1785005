# -*- coding:utf-8 -*-
'''
ts = "1495181015.03246"
its = float(ts)

#timestamp型をDate型に変換
tt = datetime.datetime.fromtimestamp(its)
# 結果 2011-10-14 00:00:00

tss = tt + datetime.timedelta(days= 1)
'''
'''
files = []
files = glob.glob('csv\*.csv')
for f in files:
    try:
        open(f, 'r', encoding="shift-jis")
        print("ok\n")
    # 起こりそうな例外をキャッチ
    except FileNotFoundError as e:
        print(e)    
'''
'''
var = []
var.append(["tsukiji","hoge1",12345])
var.append(["kasai","hoge1",134567])
var.append(["tsukiji","hoge2",76453])
var.append(["kasai","hoge2",452])
var.append(["tsukiji","hoge3",186534])
var.append(["kasai","hoge3",65343])
var2 = sorted(var, key=lambda  x:(x[0],x[2]))
#print(var2)
'''
'''
dic = []*2
for i in var:
    if(i[0] == "tsukiji"):
        dic.append({"tsukiji":{"name":i[0],"message":i[1],"int":i[2]}})
    else:
        dic.append({"kasai": {"name": i[0], "message": i[1], "int": i[2]}})
print(dic)

import codecs,json
fm = codecs.open("memberlist.json","r","utf-8")
memberlist = json.load(fm)

print(memberlist)
'''

#csvファイルから人ごとに月日(現状では年と月を表示させるプログラム)
#今後の改良として、月ごとに細分化することで時系列を意識した専門単語を抽出できるように行う。

'''
import datetime
import csv, sys, codecs, re

inputfilename = sys.argv[1]
file = codecs.open(inputfilename, 'r', encoding="utf-8")
inputfilename = re.sub("\.[a-z]+","",inputfilename)

read_txt = file.readlines()

for i in read_txt:
    #,区切りで分割してリスト化
    res = i.split(",")
    thisdate = re.sub("\\r\\n","",res[2])
    thisdate = datetime.datetime.strptime(thisdate,'%Y-%m-%d %H:%M:%S.%f')
    print(thisdate.month)


d = datetime.datetime.today()
print(d.month)

'''

dataset={}
hoge1 = [{"word":"A","num":10},{"word":"B","num":20},{"word":"C","num":30}]
hoge2 = [{"word":"D","num":40},{"word":"E","num":50},{"word":"F","num":60}]
hoge3 = [{"word":"G","num":70},{"word":"H","num":80},{"word":"I","num":90}]

dataset["tsukiji"] = hoge1
dataset["tsukiji2"] = hoge2
dataset["tsukiji3"] = hoge3

print(dataset)