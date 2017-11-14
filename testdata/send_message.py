# -*- coding: utf-8 -*-
#APIを使って対象のチャンネルのログをjson形式で取得するプログラム
import sys,codecs,json
from slacker import Slacker

# API token tokenが入ったファイルの読み込みをして取得(セキュリティ回避)
token = codecs.open("../../slackapi_token_thesis.txt", "r","utf-8")
slack = Slacker(token)

#username:bot名，icon_emoji:botのアイコン

#bot1
#slack.chat.post_message('#experiment1','e-learnning、英語',username="bot1",icon_emoji=':goat:')
#slack.chat.post_message('#experiment1','e-learnning、英語、API、中間発表',username="bot1",icon_emoji=':goat:')
#slack.chat.post_message('#experiment1','英語、リスニング、API',username="bot1",icon_emoji=':goat:')
#slack.chat.post_message('#experiment1','javascript、音声、オープンキャンパス',username="bot1",icon_emoji=':goat:')
#slack.chat.post_message('#experiment1','音声、javascript、文化祭',username="bot1",icon_emoji=':goat:')
#slack.chat.post_message('#experiment1','e-learnning、javascript、php、卒論執筆',username="bot1",icon_emoji=':goat:')
#slack.chat.post_message('#experiment1','発音、音声、英語、php',username="bot1",icon_emoji=':goat:')
#slack.chat.post_message('#experiment1','発音、API、php',username="bot1",icon_emoji=':goat:')
#slack.chat.post_message('#experiment1','javascript、API、中間発表',username="bot1",icon_emoji=':goat:')

#bot2
#slack.chat.post_message('#experiment1','Python、Web、スクレイピング',username="bot2",icon_emoji=':cow2:')
#slack.chat.post_message('#experiment1','Python、Web、スクレイピング、php、中間発表',username="bot2",icon_emoji=':cow2:')
#slack.chat.post_message('#experiment1','php、形態素解析',username="bot2",icon_emoji=':cow2:')
#slack.chat.post_message('#experiment1','php、形態素解析、mecab、オープンキャンパス',username="bot2",icon_emoji=':cow2:')
#slack.chat.post_message('#experiment1','tf-idf、slideshare、文化祭',username="bot2",icon_emoji=':cow2:')
#slack.chat.post_message('#experiment1','php、tf-idf、slideshare、卒論執筆',username="bot2",icon_emoji=':cow2:')
#slack.chat.post_message('#experiment1','API、json',username="bot2",icon_emoji=':cow2:')
#slack.chat.post_message('#experiment1','mysql、プロキシ、ファイアウォール',username="bot2",icon_emoji=':cow2:')
#slack.chat.post_message('#experiment1','協調フィルタリング、python、中間発表',username="bot2",icon_emoji=':cow2:')

#bot3
#slack.chat.post_message('#experiment1','プログラミング、GitHub',username="bot3",icon_emoji=':cat2:')
#slack.chat.post_message('#experiment1','プログラミング、GitHub、Go、中間発表',username="bot3",icon_emoji=':cat2:')
#slack.chat.post_message('#experiment1','GitHub、API、Go、Ruby、プログラミング、コンパイル',username="bot3",icon_emoji=':cat2:')
#slack.chat.post_message('#experiment1','Ruby、プログラミング、コンパイル、オープンキャンパス',username="bot3",icon_emoji=':cat2:')
#slack.chat.post_message('#experiment1','サーバ構築、linux、GitHub、文化祭',username="bot3",icon_emoji=':cat2:')
#slack.chat.post_message('#experiment1','Linux、caffe、卒論執筆',username="bot3",icon_emoji=':cat2:')
#slack.chat.post_message('#experiment1','Linux、機械学習、ファイアウォール',username="bot3",icon_emoji=':cat2:')
#slack.chat.post_message('#experiment1','mysql、プロキシ、ファイアウォール',username="bot3",icon_emoji=':cat2:')
#slack.chat.post_message('#experiment1','Linux、障害回復、自動生成、中間発表',username="bot3",icon_emoji=':cat2:')

#bot4
#slack.chat.post_message('#experiment1','データベース、学習',username="bot4",icon_emoji=':dog2:')
#slack.chat.post_message('#experiment1','音声、学習、データベース',username="bot4",icon_emoji=':dog2:')
#slack.chat.post_message('#experiment1','音声、英語、学習、e-learnning',username="bot4",icon_emoji=':dog2:')
#slack.chat.post_message('#experiment1','音声、録音、php、e-learnning、英語',username="bot4",icon_emoji=':dog2:')
#slack.chat.post_message('#experiment1','音声、録音、php、英語、中間発表',username="bot4",icon_emoji=':dog2:')

#bot5
#slack.chat.post_message('#experiment1','データ、学習、英単語',username="bot5",icon_emoji=':rabbit2:')
#slack.chat.post_message('#experiment1','英語、学習、e-learnnig',username="bot5",icon_emoji=':rabbit2:')
#slack.chat.post_message('#experiment1','英単語、発音、API',username="bot5",icon_emoji=':rabbit2:')
#slack.chat.post_message('#experiment1','API、スクレイピング、html',username="bot5",icon_emoji=':rabbit2:')
#slack.chat.post_message('#experiment1','API、スクレイピング、中間発表',username="bot5",icon_emoji=':rabbit2:')

#bot6
#slack.chat.post_message('#experiment1','プログラミング、学習、GiHhub',username="bot6",icon_emoji=':chipmunk:')
#slack.chat.post_message('#experiment1','Linux、学習、GitHub',username="bot6",icon_emoji=':chipmunk:')
#slack.chat.post_message('#experiment1','Web、プログラミング、Linux',username="bot6",icon_emoji=':chipmunk:')
#slack.chat.post_message('#experiment1','文字取得、Web、API',username="bot6",icon_emoji=':chipmunk:')
#slack.chat.post_message('#experiment1','Linux、API、作成、中間発表',username="bot6",icon_emoji=':chipmunk:')

#bot7
#slack.chat.post_message('#experiment1','Web、プログラミング',username="bot7",icon_emoji=':dragon:')
#slack.chat.post_message('#experiment1','コンパイラ、JavaScript',username="bot7",icon_emoji=':dragon:')
#slack.chat.post_message('#experiment1','JavaScript、php',username="bot7",icon_emoji=':dragon:')
#slack.chat.post_message('#experiment1','php、Linux',username="bot7",icon_emoji=':dragon:')
#slack.chat.post_message('#experiment1','Linux、API',username="bot7",icon_emoji=':dragon:')