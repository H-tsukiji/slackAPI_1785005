# -*- coding: utf-8 -*-
import json,codecs
from datetime import datetime

f = codecs.open("testdata.json","r","utf-8")
logs = json.load(f)

#ログデータのタイムスタンプを基に月日ごとに分類する
t_data = {}
for log in logs:
    #print(log["ts"])
    log_ts = datetime.fromtimestamp(float(log["ts"]))
    #print(log_ts.month,log_ts.day)
    if log_ts.month not in t_data:
        if log_ts.day not in t_data:
            t_data = {log_ts.month:{log_ts.day:[]}}
            t_data[log_ts.month][log_ts.day].append(log)
    else:
        if log_ts.day not in t_data[log_ts.month]:
            t_data[log_ts.month].update({log_ts.day:[]})
            t_data[log_ts.month][log_ts.day].append(log)
        else:
            t_data[log_ts.month][log_ts.day].append(log)
print(t_data)