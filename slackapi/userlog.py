# -*- coding: utf-8 -*-
#log_sum.pyでまとめたログをユーザ毎に分解していく
import csv, sys, MeCab, re

#対象ファイルの取得および分かち書きの設定
inputfilename = sys.argv[1]
file = open(inputfilename, 'r', encoding="utf-8")
inputfilename = re.sub("\.[a-z]+","",inputfilename)
csvdata = csv.reader(file)

logindex = []

for row in csvdata:
    userfile = open("txt/"+row[0]+".txt","a",encoding="utf-8")
    userfile.write(row[1]+","+row[2]+","+row[3]+"\n")

userfile.close()