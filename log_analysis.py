# -*- coding: utf-8 -*-

import codecs,json

#ログのJSONファイルの読み込み
f = codecs.open("slack.json","r","utf-8")
f_json = json.load(f)
