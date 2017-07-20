# -*- coding:utf-8 -*-

import datetime,glob

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

var = []
var.append(["tsukiji","hoge1",12345])
var.append(["kasai","hoge1",134567])
var.append(["tsukiji","hoge2",76453])
var.append(["kasai","hoge2",452])
var.append(["tsukiji","hoge3",186534])
var.append(["kasai","hoge3",65343])

var2 = sorted(var, key=lambda  x:(x[0],x[2]))

print(var2)



'''
dic = []*2
for i in var:
    if(i[0] == "tsukiji"):
        dic.append({"tsukiji":{"name":i[0],"message":i[1],"int":i[2]}})
    else:
        dic.append({"kasai": {"name": i[0], "message": i[1], "int": i[2]}})
print(dic)
'''


