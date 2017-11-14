# -*- coding: utf-8 -*-
import json,codecs
from datetime import datetime

f = codecs.open("experiment1.json","r","utf-8")
logs = json.load(f)

namelist=[]

for log in logs:
    if log["name"] not in namelist:
        namelist.append(log["name"])

for name in namelist:
    index = []
    word_index = {}
    for log in logs:
        if log["name"] == name:
            for word in log["text"].split("、"):
                if word not in index:
                    index.append(word)
                    word_index[word]=1
                else:
                    word_index[word] += 1
        sorted(word_index.items(),key=lambda x: x[1])
        #JSON形式に変換しファイルに出力
        f = codecs.open(name+".json","w","utf-8")
        f.write(json.dumps(word_index,indent=3,ensure_ascii=False));
        f.close()

