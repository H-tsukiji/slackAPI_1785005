# -*- coding: utf-8 -*-
import codecs,csv,re,math
import numpy as np

user_index = ["@bot1", "@bot2", "@bot3", "@bot4", "@bot5", "@bot6", "@bot7"]

#csvデータを読み込む関数
#返り値はbot1{{time:ti,text:""},...,}の配列になる
def Reading_csvfile():
    f = codecs.open("sessiondata.csv","r",encoding="utf-8")
    reader = csv.reader(f)
    header = next(reader)
    csv_data = {}
    for row in reader:
        if (row[0] not in csv_data) == True :
            csv_data[row[0]] = []
        csv_data[row[0]].append({"time":row[1],"text":row[2]})
    f.close()
    return csv_data



if __name__ == '__main__':
    user_data = Reading_csvfile()
    print(user_data['bot1'][0]['text'])

    #他のユーザに言われた会話内容を記録する
    for user in user_index:     
        for i in user_data:
            for j in user_data[i]:
                if (user in j['text']) == True:
                    print('ok')
                else:
                    continue