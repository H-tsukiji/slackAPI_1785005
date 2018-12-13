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

def Leader_score(parameter_list):
    mention_data = Read_Mention_file()
    reaction_data = Read_reaction_file()
    thread_data = Read_thread_file()


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


