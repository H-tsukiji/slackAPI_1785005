# -*- coding: utf-8 -*-
import codecs,csv,re,math,os,sys,glob,json,gc
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


if __name__ == "__main__":

    #csvのフォルダ名指定
    folder_name = sys.argv[1]

    #csvファイルの取得
    files = []
    files = glob.glob(folder_name+'/*.csv')

    #wordindex:出現するすべての単語リスト
    #data_set:データセットユーザ毎に単語のカウントデータを入れるない場合は0を入れる
    word_index = []
    cosdata_set = []
    word_index = Read_wakachidata(files)
    cosdata_set = Make_uservector(files, word_index)

    #コサイン類似度出すまでの一連の処理
    cos_data = np.array(cosdata_set)
    cos_data = cos_data.astype(np.int)
    cos_result = cos_sim_matrix(cos_data)
    print(cos_result)




