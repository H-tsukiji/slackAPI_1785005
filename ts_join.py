# -*- coding: utf-8 -*-

import codecs, json, csv
from datetime import datetime
#ログのJSONファイルの読み込み
f = open("log_general_channel.csv","r")
fgeneral = csv.reader(f)
f = open("log_report_channel.csv","r")
freport = csv.reader(f)
f = open("log_seminar1421_channel.csv","r")
fseminar = csv.reader(f)
f4 = open("log_grad2017_channel.csv","rb")
fgrad = csv.reader(f4)
fm = codecs.open("memberlist.json","r","utf-8")
memberlist = json.load(fm)

print(fgrad)



