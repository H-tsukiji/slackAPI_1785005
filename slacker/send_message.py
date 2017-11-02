# -*- coding: utf-8 -*-
#APIを使って対象のチャンネルのログをjson形式で取得するプログラム
import sys,codecs,json
from slacker import Slacker

# API token tokenが入ったファイルの読み込みをして取得(セキュリティ回避)
token = codecs.open("../../slackapi_token_thesis.txt", "r","utf-8")
slack = Slacker(token)

#username:bot名，icon_emoji:botの
#slack.chat.post_message('#general','H',username="bot1",icon_emoji=':goat:')
#slack.chat.post_message('#general','e',username="bot2",icon_emoji=':cow2:')
#slack.chat.post_message('#general','l',username="bot3",icon_emoji=':cat2:')
#slack.chat.post_message('#general','l',username="bot4",icon_emoji=':dog2:')
slack.chat.post_message('#general','o',username="bot5",icon_emoji=':rabbit2:')