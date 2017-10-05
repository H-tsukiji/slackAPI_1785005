# -*- coding: utf-8 -*-
import os,sys,glob,json,codecs,gc

dirname = sys.argv[1]

#ファイルパスの取得
filepathlist = glob.glob(dirname+'/*')

#wordindex:出現するすべての単語リスト
#data_set:データセットユーザ毎に単語のカウントデータを入れるない場合は0を入れる
wordindex = []
data_set = {}
tmpwordlist = []

#wordindexに単語を登録
#調整：キーのみを抽出してインデックスにしていく
for path in filepathlist:
    f = codecs.open(path,"r","utf-8")
    fjson = json.load(f)
    tmpkey = fjson.keys()
    for word in tmpkey:
        if ((word in wordindex) == False):
            wordindex.append(word)
        else:
            continue
f.close()

#データセットの作成
for path in filepathlist:
    f = codecs.open(path,"r","utf-8")
    fjson = json.load(f)
    tmpkey =fjson.keys()
    #ユーザ名の取得
    username = os.path.splitext(os.path.basename(path))
    for word in wordindex:
        if (word in tmpkey) == False :
                tmpwordlist.append({"word":word,"count":0})
        else:
            tmpwordlist.append({"word":word,"count":fjson[word]})
    #ここでデータセットに入れる
    data_set[username[0]] = tmpwordlist
    tmpwordlist = []
    tmpkey = []
f.close()

#テストファイルの出力
fp = codecs.open("dataset.json","w","utf-8")
fp.write(json.dumps(data_set,indent=1));
fp.close()
