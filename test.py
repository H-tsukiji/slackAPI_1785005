# -*- coding:utf-8 -*-

import datetime

ts = "1495181015.03246"
its = float(ts)

#timestamp型をDate型に変換
tt = datetime.datetime.fromtimestamp(its)
# 結果 2011-10-14 00:00:00

tss = tt + datetime.timedelta(days= 1)

print(tt)
print(tss)