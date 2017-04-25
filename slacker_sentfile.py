# -*- coding: utf-8 -*-

import sys,codecs
from slacker import Slacker

# API token tokenが入ったファイルの読み込みをして取得(セキュリティ回避)
token = codecs.open("../slackapi_token.txt", "r","utf-8")

 
# 投稿するチャンネル名
c_name = '@tsukiji'
 
# 投稿する画像ファイルへのパス(パラメタから取得) 相対パス
#f_path = sys.argv[1]
 
# 投稿
slacker = Slacker(token)
slacker.chat.post_message(c_name, '画像アップするよ', as_user=True)
#slacker.files.upload(f_path, channels=[c_name], title='タイトル')