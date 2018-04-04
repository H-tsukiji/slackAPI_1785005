# -*- coding: utf-8 -*-

import sys, codecs, json
from slacker import Slacker

# API token tokenが入ったファイルの読み込みをして取得(セキュリティ回避)
token = codecs.open("../slackapi_token.txt", "r", "utf-8")

# logの取得を送る　token,指定チャンネルid,タイムスタンプの有無などを条件付けする
# 返しはインスタンス変数になってる(？)
slacker = Slacker(token)
# 中身を取りたいなら、.bodyを付ける事！！！！
result = slacker.users.list().body;

member =[]
count = 0;


for i in result["members"]:
    member.append({"id":i["id"],"name":i["name"]})


print(member)


#JSON形式に変換しファイルに出力
f = codecs.open("memberlist.json","w","utf-8")
f.write(json.dumps(member,indent=1));
f.close()
