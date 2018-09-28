# -*- coding: utf-8 -*-
#APIを使って対象のチャンネルのログをjson形式で取得するプログラム
import sys,codecs,json
from slacker import Slacker

# API token tokenが入ったファイルの読み込みをして取得(セキュリティ回避)
token = codecs.open("../../slackapi_token.txt", "r","utf-8")

# 対象のチャンネル名
# general:C0J8KM6KF  
# 2017-sotsuken:C18JT8ZNY  
# report:C0XMH9F0Q  
# master-chat:C4W2RL2BA
# chat:C0J8Q0DK9 
# 2018-4-sotsuken:C9EJZ0MMJ
c_name = 'C4W2RL2BA'

 
# logの取得を送る　token,指定チャンネルid,タイムスタンプの有無などを条件付けする
# 返しはインスタンス変数になってる(？)
slacker = Slacker(token)
#中身を取りたいなら、.bodyを付ける事！！！！
result = slacker.channels.history(c_name,count=1000).body

#print(result)
"""
ここで分かったこと
vars()で文字列化するといろいろと出力結果がカバる
(シングルクォーテーションやないのが混在してJSON形式にして分析しやすいようにできない)
slackerパッケージの関数の最後に.bodyとくっつけることで，オブジェクトの中身を取得することができる！！！！

"""
#JSON形式に変換しファイルに出力
f = codecs.open("..\slack_"+c_name+".json","w","utf-8")
f.write(json.dumps(result,indent=3,ensure_ascii=False));
f.close()
