# -*- coding: utf-8 -*-
#ユーザが指定したリプライのカウントを行うプログラム
import sys,re,codecs,json,os

inputfile = sys.argv[1]
file = open(inputfile, 'r', encoding="utf-8")
fline = file.readlines()
file.close()

#ファイル名を名前だけ抜き取る
username = os.path.basename(inputfile)
username = re.sub("\.txt","",username)

re_index = {}
for line in fline:
    #ユーザ指定のタグを検知する正規表現<@U0JACJLRJ>や<@U0J8PMAQJ|t.kasai>
    reget = "<@\S+>"
    matchtext = re.finditer(reget,line)
    if matchtext:
        for result in matchtext:
            key = result.group()
            """
            relef = "\|\w+"
            key = re.sub(relef,"",key)
            """
            if (key in re_index) == False:
                re_index[key] = 1
            else:
                re_index[key] = re_index[key] + 1

re_index = sorted(re_index.items(), key=lambda x:x[1],reverse=True)

#JSON形式に変換しファイルに出力
f = codecs.open("txt/rep_"+username+".json","w","utf-8")
f.write(json.dumps(re_index,indent=1));
f.close()


"""
やんないといけないこと
最初に引数のファイル名を名前だけ抜き取って出力ファイルの名前にできるように調整
<@U0JAEV08K|tsukiji>を<@U0JAEV08K>に直すように調整する
どちらも正規表現で調整する事
relef = "|\w+"
        if matchtext.find(relef) :
            matchtext = re.sub(relef,"",matchtext)
"""