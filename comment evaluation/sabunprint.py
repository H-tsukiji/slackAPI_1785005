# -*- coding: utf-8 -*-

import codecs,sys,re,MeCab

filename = sys.argv[1]
f = codecs.open(filename, "r", "utf-8")

#txtから文章を格納
diff_text = ""
for line in f:
    if re.search("^\+",line):
        line = re.sub("\+","",line)
        diff_text += line
    else:
        continue
#print(diff_text)

