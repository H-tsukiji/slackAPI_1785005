# -*- coding: utf-8 -*-

import codecs,json

#ログのJSONファイルの読み込み
f = codecs.open("slack.json","r","utf-8")
f_json = json.load(f)

index_username = []
index = []
count = 0

#隔離
#まずはf_json["messages"]["user"]の中身が取れているのか確認
"""
for i in f_json["messages"]:
    if f_json["messages"]["user"] in index_username:
        index_username.append(f_json["messages"]["user"])
    else:
        count += 1

print(count)
"""
