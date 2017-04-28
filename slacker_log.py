# -*- coding: utf-8 -*-

import sys,codecs,json,pprint
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
#中身を取りたいなら、.bodyを付ける事！！！！
result = slacker.channels.history(c_name,count=5).body

"""
ここで分かったこと
vars()で文字列化するといろいろと出力結果がカバる
(シングルクォーテーションやないのが混在してJSON形式にして分析しやすいようにできない)
slackerパッケージの関数の最後に.bodyとくっつけることで，オブジェクトの中身を取得することができる！！！！
"""

#JSON形式に変換しファイルに出力
f = codecs.open("slack.json","w","utf-8")
f.write(json.dumps(result,indent=3));
f.close()
