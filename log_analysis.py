# -*- coding: utf-8 -*-

import codecs,json

f = codecs.open("slack.json","r","utf-8")
#文字列として読み込む
f_str = f.read()

#なぜかシングルクォーテーションの部分を
#ダブルクォーテーションに置換
f_strjson = f_str.replace('\'','\"')

f_json = json.loads(f_strjson)