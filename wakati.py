# -*- coding: utf-8 -*-
import csv, sys, MeCab, re

'''
log_sum.pyより生成したslacklog.csvファイルを読み込み
分かち書きを行うプログラム
この際、csvファイルにあるユーザ名よりそれぞれに対応したファイルに書き込まれる
出力はユーザ名.txtでありcsvファイルを基に作られる。
引数はslacklog.csvである
'''

#対象ファイルの取得および分かち書きの設定
inputfilename = sys.argv[1]
file = open(inputfilename, 'r', encoding="utf-8")
inputfilename = re.sub("\.[a-z]+","",inputfilename)
#output = open(inputfilename+"_wakati.txt", 'w', encoding="utf-8")
tagger = MeCab.Tagger("-Owakati")
csvdata = csv.reader(file)

#1行づつ読み込みノイズとなるような記号とひらがなを排除
def cleanInput(text):

    if (len(text)== 1):
        text = re.sub(r'\w', ' ', text)

    else:
        text = re.sub('\n', ' ', text)
        text = re.sub(r'[.,･%$&#:;＆。※↑↓→←、．…，：；＾？～￥「」（）()【】『』<>・_=|?［］\[\]\"\']', ' ', text)
        text = re.sub(r'[@＠]\w+', ' ', text)
        text = re.sub(r'[0-9]', ' ', text)
        text = re.sub(r'[０-９]', ' ', text)
        text = re.sub('-', ' ', text)
        text = re.sub('/', ' ', text)
        text = re.sub('\r\n', ' ', text)
        text = re.sub('　', ' ', text)
        text = re.sub('[ぁ-ん]', ' ', text)
    return text

def writetext(line):
    if(len(line) == 1):
        pass
    output.write(line + "\n")



index = []
#txtファイルの作成
for row in csvdata:
    if ((row[0] in index) == False):
        index.append(row[0])
        output = open("txt\\wakati\\" + row[0] + ".txt", 'w', encoding="utf-8")
        w_text = cleanInput(row[1])
        w_text = tagger.parse(w_text)
        writetext(w_text)
    else:
        w_text = cleanInput(row[1])
        w_text = tagger.parse(w_text)
        writetext(w_text)

file.close()
output.close()
