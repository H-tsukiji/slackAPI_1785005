# -*- coding: utf-8 -*-

import sys,codecs
from slacker import Slacker

# API token tokenが入ったファイルの読み込みをして取得(セキュリティ回避)
token = codecs.open("../slackapi_token.txt", "r","utf-8")

# 対象のチャンネル名
c_name = 'C0J8KM6KF'
 
# 投稿する画像ファイルへのパス(パラメタから取得) 相対パス
#f_path = sys.argv[1]
 
# 投稿
slacker = Slacker(token)
result = slacker.channels.history(c_name,inclusive=True,unreads=True)
#slacker.files.upload(f_path, channels=[c_name], title='タイトル')


print(vars(result))