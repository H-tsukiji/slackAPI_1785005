# -*- coding: utf-8 -*-
#APIを使って対象のチャンネルのログをjson形式で取得するプログラム
import sys,codecs,json
from slacker import Slacker

# API token tokenが入ったファイルの読み込みをして取得(セキュリティ回避)
token = codecs.open("../../slackapi_token_thesis.txt", "r","utf-8")

# 対象のチャンネル名
# general:C7TP92V60, experiment1:C7WMQ5E2C
c_name = 'C7WMQ5E2C'

# logの取得を送る　token,指定チャンネルid,タイムスタンプの有無などを条件付けする
# 返しはインスタンス変数になってる(？)
slacker = Slacker(token)
#中身を取りたいなら、.bodyを付ける事！！！！
result = slacker.channels.history(c_name,count=1000).body


log = []
for message in result['messages']:
    if ("username" in message) == False:
        continue
    log.append({"name":message["username"],"text":message["text"],"ts":message["ts"]})


#JSON形式に変換しファイルに出力
f = codecs.open("experiment1.json","w","utf-8")
f.write(json.dumps(log,indent=3,ensure_ascii=False));
f.close()