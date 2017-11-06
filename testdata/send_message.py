# -*- coding: utf-8 -*-
#APIを使って対象のチャンネルのログをjson形式で取得するプログラム
import sys,codecs,json
from slacker import Slacker

# API token tokenが入ったファイルの読み込みをして取得(セキュリティ回避)
token = codecs.open("../../slackapi_token_thesis.txt", "r","utf-8")
slack = Slacker(token)

#username:bot名，icon_emoji:botの
#slack.chat.post_message('#general','test6',username="bot1",icon_emoji=':goat:')
slack.chat.post_message('#general','hogehoge',username="bot2",icon_emoji=':cow2:')
#slack.chat.post_message('#general','test4',username="bot3",icon_emoji=':cat2:')
#slack.chat.post_message('#general','test3',username="bot4",icon_emoji=':dog2:')
#slack.chat.post_message('#general','test2',username="bot5",icon_emoji=':rabbit2:')
#slack.chat.post_message('#general','test',username="bot6",icon_emoji=':chipmunk:')