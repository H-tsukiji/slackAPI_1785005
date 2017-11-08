# -*- coding: utf-8 -*-
import json,codecs
from datetime import datetime

f = codecs.open("testdata.json","r","utf-8")
logs = json.load(f)

ts = []
for i in logs:
    ts.append(datetime.fromtimestamp(float(i["ts"])))

#好きな日時を指定
d1 = datetime(2017,11,6,hour=14,minute=35)
#日時の比較(datetime型)
print(ts[0] > d1)

print(ts[0])
print(ts[1])