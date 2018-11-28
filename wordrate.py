# -*- coding: utf-8 -*-
#各チャンネルのログを統合し、まとめたログの作成
import codecs,json,csv,glob,re



#フォルダcsv内にあるすべてのcsvファイルを取得する。
files = []
files = glob.glob('slackapi/20180925/*.csv')

f_in = codecs.open("word.txt","r","utf-8")
lines = f_in.readlines()

word_index = []
for line in lines:
    line = re.sub('\r\n', '', line)
    word_index.append(line) 


if __name__ == '__main__':
    #print(word_index)

    for csvfile in files:
        file = open(csvfile, 'r', encoding="utf-8")
        csvdata = csv.reader(file)

        print(csvfile)
        total = 0
        ex_total = 0
        for row in csvdata:
            total += int(row[1])
            if row[0] not in word_index:
                continue
            else:
                ex_total += int(row[1])
                #print(row[0])
        rate = ex_total / total
        print("専門単語使用回数：",ex_total)
        print("総単語使用回数：",total)
        print("専門単語割合：",rate)
                    
