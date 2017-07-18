# -*- coding:utf-8 -*-

import datetime

ts = "1495181015.03246"
its = float(ts)

#timestamp型をDate型に変換
tt = datetime.datetime.fromtimestamp(its)
# 結果 2011-10-14 00:00:00

tss = tt + datetime.timedelta(days= 1)


list = {'no':1,'messages': [
    {'type': 'message', 'user': 'U0JACJLRJ', 'text': '院生はどこ？', 'ts': '1499914704.048466'},
    {'type': 'message', 'user': 'U0JAEV08K', 'text': '他にも探しましが、めぼしいものはこれぐらいでしたね・・・', 'ts': '1499339408.840567'},
    {'type': 'message', 'user': 'U0JACJLRJ', 'text': 'update-grubは、今日はやってないですね。', 'ts': '1499338936.701231'},
    {'type': 'message', 'user': 'U0JACJLRJ', 'text': 'ありがとう、明日試してみます。', 'ts': '1499338903.691362'}
    ]}

print(sorted(list['messages']['ts'],reverse=True))