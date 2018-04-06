# -*- coding: utf-8 -*-
import codecs,csv,re,math,MeCab
import numpy as np

user_index = ["bot1", "bot2", "bot3", "bot4", "bot5", "bot6", "bot7"]

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

def Receive_message(user_data):
    receive = {}
    for user in user_index:
        for i in user_data:
            if i not in receive:
                receive[i] = []
            for j in user_data[i]:
                if (user in j['text']) == True:
                    receive[user].append(j['text'])
    return receive

def Mecab_wakati(word_list):
    t = []
    for user in word_list:
        for text in word_list[user]:
            wakati = CleanInput(text)
            wakati = tagger.parse(text)
            t.append(wakati)
    print(t)

def CleanInput(text):
    text = re.sub('\n', ' ', text)
    text = re.sub(r'[.,･%$&#:;＆。※↑↓→←、．，：；＾？～￥「」（）()【】『』<>・_=|?［］\[\]\"\']', ' ', text)
    text = re.sub(r'[@＠]\w+', ' ', text)
    text = re.sub(r'[0-9]', ' ', text)
    text = re.sub(r'[０-９]', ' ', text)
    text = re.sub('-', ' ', text)
    text = re.sub('/', ' ', text)
    text = re.sub('\r\n', ' ', text)
    text = re.sub('　', ' ', text)
    #text = re.sub('[ぁ-ん]', ' ', text)
    return text

if __name__ == '__main__':
    user_data = Reading_csvfile()

    message_receive = {}
    message_send = {}

    tagger = MeCab.Tagger("-Owakati")

    #他のユーザから来たメッセージを記録する
    message_receive = Receive_message(user_data)
    #print(message_receive["bot6"])
    #他のユーザに送ったメッセージを記録する
    message_send = Send_message(user_data)
    #print(message_send)

    test = {'botx':["あめんぼあかいなあいうえお","飛んで火にいる夏の虫"]}

    Mecab_wakati(message_receive)

