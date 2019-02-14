# -*- coding: utf-8 -*-
import codecs,json,csv,sys,re
from datetime import datetime

#対象ファイルの取得および分かち書きの設定
inputfilename = sys.argv[1]
file = open(inputfilename, 'r', encoding="utf-8")
inputfilename = re.sub("\.[a-z]+","",inputfilename)
csvdata = csv.reader(file)

for row in csvdata:
    userfile = open("20190214/"+row[0]+"_messages.txt","a",encoding="utf-8")
    userfile.write(row[1]+"\n")
userfile.close()
