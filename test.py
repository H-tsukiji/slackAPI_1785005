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
'''
'''
csvファイルから人ごとに月日(現状では年と月を表示させるプログラム)
今後の改良として、月ごとに細分化することで時系列を意識した専門単語を抽出できるように行う。
'''
from datetime import *
import csv, sys, MeCab, re

inputfilename = sys.argv[1]
file = open(inputfilename, 'r', encoding="utf-8")
inputfilename = re.sub("\.[a-z]+","",inputfilename)
csvdata = csv.reader(file)

index = []

for i,row in enumerate(csvdata):
    if(i == 0):
        continue

    if ((row[0] in index) == False):
        index.append(row[0])
        tmp = datetime.fromtimestamp(float(row[2]))
        print(row[0])
        print(tmp.year," ",tmp.month)
    else:
        tmp = datetime.fromtimestamp(float(row[2]))
        print(tmp.year," ",tmp.month)

'''
def one_strskip (line):
    if(len(line) == 1):
        print("ok\n")
    else:
        print("no\n")


str_t = ["あいあいあいいあ","の","ののｎ"," "]

for i in str_t:
    one_strskip(i)
'''