# -*- coding: utf-8 -*-
import codecs,csv,re,math,os,sys,glob,json
import numpy as np


def Read_wakachidata(files):
    #wordindexに単語を登録
    #調整：キーのみを抽出してインデックスにしていく
    wordindex = []
    
    for csvfile in files:
        f = codecs.open(csvfile,"r", "utf-8")
        csvdata = csv.reader(f)
        for word in csvdata:
            if ((word[0] in wordindex) == False):
                wordindex.append(word[0])
            else:
                continue
        f.close()
    return wordindex

def Make_uservector(files,index):
    #単語頻度によるユーザベクトルの作成
    data_set = []

    for csvfile in files:
        f = codecs.open(csvfile,"r", "utf-8")
        csvdata = csv.reader(f)

        #ユーザ毎に用意される出現語句スペース
        tmpkey = []
        tmpwordlist = []
        tmpvalue = []

        for key in csvdata:
            tmpkey.append(key[0])
            tmpvalue.append(key[1])

        for word in index:
            #ユーザベクトル：ユーザにない語句は0でそれ以外はそのまま
            if (word in tmpkey) == False :
                    tmpwordlist.append(0)
            else:
                number = tmpkey.index(word)
                tmpwordlist.append(tmpvalue[number])
        #ここでデータセットに入れる
        data_set.append(tmpwordlist)
        f.close()
    return data_set

def cos_sim_matrix(matrix):
    """
    item-feature 行列が与えられた際に
    item 間コサイン類似度行列を求める関数
    """
    d = matrix @ matrix.T  # item-vector 同士の内積を要素とする行列
    # コサイン類似度の分母に入れるための、各 item-vector の大きさの平方根
    norm = (matrix * matrix).sum(axis=1, keepdims=True) ** .5
    # それぞれの item の大きさの平方根で割っている
    return d / norm / norm.T


def Cosine_similarity(csvfiles):
    '''
    コサイン類似度を算出する工程をすべて含んだ関数
    使用関数
    Read_wakachidata
    Make_uservector
    cos_sim_matrix
    '''
    #wordindex:出現するすべての単語リスト
    #data_set:データセットユーザ毎に単語のカウントデータを入れるない場合は0を入れる
    word_index = []
    cosdata_set = []
    word_index = Read_wakachidata(csvfiles)
    cosdata_set = Make_uservector(csvfiles, word_index)

    #コサイン類似度出すまでの一連の処理
    cos_data = np.array(cosdata_set)
    cos_data = cos_data.astype(np.int)
    cos_result = cos_sim_matrix(cos_data)
    print(cos_result)

def Leader_score(memberlist):
    # 各種データファイル読み込み
    mention_data = Read_Mention_file()
    reaction_data = Read_reaction_file()
    thread_data = Read_thread_file()
    jyodoshi_data = Read_jyodoshi_file()

    # メンションによる全ユーザとの平均会話数
    mention_ave = {}
    for user, values in mention_data.items():
        sum = 0
        for count in values:
            sum += int(count[1])
        mention_ave[user] = sum / len(memberlist)

    # リアクションによる全ユーザとの反応数の平均
    reaction_ave = {}
    for user, values in reaction_data.items():
        sum = 0
        for num in values.values():
            sum += int(num)
        reaction_ave[user] = sum / len(memberlist)

    # スレッドの開始となった回数
    thread_num = {}
    for user, values in thread_data.items():
        thread_num[user] = int(values['first_count'])

    # 発言内の助動詞に基づいた使役の意味を含む発言の割合
    jyodoshi_rate = {}
    for user, values in jyodoshi_data.items():
        jyodoshi_rate[user] = float(values['rate'])

    # リーダスコアの算出
    reader_score = {}
    for user in memberlist:
        username = user['name']
        reader_score[username] = 0.0
        if user['name'] in mention_ave:
            reader_score[username] += mention_ave[username]
        if user['name'] in reaction_ave:
            reader_score[username] += reaction_ave[username]
        if user['name'] in jyodoshi_rate:
            reader_score[username] += jyodoshi_rate[username]
        if user['name'] in thread_num :
            reader_score[username] += thread_num[username]
    #print(reader_score)

    print('Leader_Score')
    for key, values in reader_score.items():
        print(key)
        print(values)
        print("------")

def Support_score():

    # 各種データファイル読み込み
    mention_data = Read_Mention_file()
    reaction_data = Read_reaction_file()
    thread_data = Read_thread_file()

    # メンションによる特定のユーザとの会話数
    # mention_data 誰が誰にメンションしたかの回数

    # リアクションによる特定のユーザとの反応数
    # mention_data 誰が誰にリアクションしたかの回数

    # スレッドにて返信をした回数
    thread_send = {}
    for user, values in thread_data.items():
        thread_send[user] = int(values['send_count'])
    # print(thread_send)

    support_score = {}
    for user in memberlist:
        username = user['name']
        support_score[username] = {}
        if username in mention_data:
            for row in mention_data[username]:
                if row[0] in support_score[username]:
                    support_score[username][row[0]] += int(row[1])
                else :
                    support_score[username][row[0]] = int(row[1])
        if username in reaction_data:
            for key, values in reaction_data[username].items():
                if key in support_score[username]:
                    support_score[username][key] += int(values)
                else :
                    support_score[username][key] = int(values)
        if user['name'] in thread_send :
            # reader_score[username] += thread_num[username]
            pass
        pass

    print('Surrport_Score')
    for key, values in support_score.items():
        print("User:"+key)
        for i,j in values.items():
            print(i)
            print(j)
        print('---------------')
    

def Read_reaction_file():
    f = codecs.open("reaction_list.csv","r", "utf-8")
    csvdata = csv.reader(f)
    next(csvdata)
    reaction_data = {}
    for row in csvdata:
        if (row[0] not in reaction_data) == True:
            reaction_data[row[0]] = {}
        if (row[1] not in reaction_data[row[0]] ) == True:
            reaction_data[row[0]][row[1]] = 1
        else:
            reaction_data[row[0]][row[1]] += 1 
    f.close()
    return reaction_data

def Read_Mention_file():
    #csvファイルの取得
    mention_folder = 'rep'
    files = []
    files = glob.glob(mention_folder+'/*.csv')
    mention_data = {}
    for userfile in files:
        f = codecs.open(userfile,"r", "utf-8")
        csvdata = csv.reader(f)
        next(csvdata)
        username = os.path.basename(userfile)
        username = re.sub('rep_','',username)
        username = re.sub('_messages.csv','',username)
        mention_data[username] = []
        for row in csvdata:
            mention_data[username].append([row[0],row[1]])
        f.close()
    mention_data = sorted(mention_data.items())
    mention_data  = dict(mention_data)
    return mention_data

def Read_thread_file():
    thread_data = {}
    f = codecs.open("thread_message_countlist.csv","r", "utf-8")
    thread_file = csv.reader(f)
    next(thread_file)
    for row in thread_file:
        thread_data[row[0]] = {"send_count":row[1],"first_count":0}
    f.close()
    f = codecs.open("first_thread_user.csv","r", "utf-8")
    first_thread_file = csv.reader(f)
    next(first_thread_file)
    for row in first_thread_file:
        thread_data[row[0]]['first_count'] = row[1]
    f.close()
    return thread_data

def Read_jyodoshi_file():
    jyodoshi = {}
    f = codecs.open("jyodoshi_count.csv","r", "utf-8")
    jyodoshi_file = csv.reader(f)
    next(jyodoshi_file)
    for row in jyodoshi_file:
        jyodoshi[row[0]] = {"order_count":row[1], "total_count":row[2], "rate":row[3]}
    return jyodoshi

if __name__ == "__main__":

    #csvのフォルダ名指定
    folder_name = sys.argv[1]

    #csvファイルの取得
    files = []
    files = glob.glob(folder_name+'/*.csv')

    fm = codecs.open("memberlist.json","r","utf-8")
    memberlist = json.load(fm)
    fm.close()

    #コサイン類似度算出
    Cosine_similarity(files)

    # リーダスコアの算出
    Leader_score(memberlist)
    
    #サポート性の算出
    Support_score()

