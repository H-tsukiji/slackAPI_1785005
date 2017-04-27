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
result = slacker.channels.history(c_name,count=5)


"""
ここで分かったこと
vars()で文字列化するといろいろと出力結果がカバる
(シングルクォーテーションやないのが混在してJSON形式にして分析しやすいようにできない)
なとかしないとつらみ
"""

hoge = str(vars(result))

#JSON形式に変換しファイルに出力
f = codecs.open("slack.json","w","utf-8")
f.write(hoge);

#とりあえず表示させる
#print(vars(result))
