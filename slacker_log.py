# -*- coding: utf-8 -*-

import sys,codecs,json
from slacker import Slacker

# API token tokenが入ったファイルの読み込みをして取得(セキュリティ回避)
token = codecs.open("../slackapi_token.txt", "r","utf-8")

# 対象のチャンネル名
c_name = 'C0J8KM6KF'
 
# 投稿する画像ファイルへのパス(パラメタから取得) 相対パス
#f_path = sys.argv[1]
 
# logの取得を送る　token,指定チャンネルid,タイムスタンプの有無などを条件付けする
# 返しはインスタンス変数になってる(？)
slacker = Slacker(token)
result = slacker.channels.history(c_name,count=5,inclusive=True,unreads=True)

#listに突っ込む
log = []
log.append(result)


f = codecs.open("slack.json","w","utf-8")

f.write(json.dumps(log));



#とりあえず表示させる
#print(vars(result))