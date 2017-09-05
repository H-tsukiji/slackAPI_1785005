# -*- coding: utf-8 -*-

import sys, codecs, json
from slacker import Slacker

# API token tokenが入ったファイルの読み込みをして取得(セキュリティ回避)
token = codecs.open("../slackapi_token.txt", "r", "utf-8")
channel = sys.argv[1]

# logの取得を送る　token,指定チャンネルid,タイムスタンプの有無などを条件付けする
# 返しはインスタンス変数になってる(？)
slacker = Slacker(token)

# 中身を取りたいなら、.bodyを付ける事！！！！
result = slacker.channels.info(channel).body

member = {}
member["channel_id"] = result['channel']['id']
member["channel_name"] = result['channel']['name']
member["member"] = result['channel']['members']

#JSON形式に変換しファイルに出力
f = codecs.open(channel+".json","w","utf-8")
f.write(json.dumps(member,indent=3));
f.close()