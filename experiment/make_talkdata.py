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

def Send_message(user_data):
    #他のユーザに送ったメッセージを記録する
    send = {}
    for user in user_index:
        for i in user_data:
            if i not in send:
                send[i] = []
            for j in user_data[i]:
                if (user in j['text']) == True:
                    send[i].append(j['text'])
    return send

def Receive_message(self, parameter_list):
    pass


if __name__ == '__main__':
    user_data = Reading_csvfile()

    message_receive = {}
    message_send = {}

    #他のユーザに言われた会話内容を記録する

    #他のユーザに送ったメッセージを記録する
    message_send = Send_message(user_data)
    #print(message_send)