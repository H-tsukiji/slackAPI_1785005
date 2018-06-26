# -*- coding: utf-8 -*-

import codecs, json, sys, re

filename = sys.argv[1]
f = codecs.open(filename,"r","utf-8")
fjson = json.load(f)


def cleantitle(title):
    title = re.sub(' ','', title)
    title = re.sub('/','', title)
    return title

for issue in fjson["issues"]["edges"]:
    issuedic = []
    #イシューのタイトル
    title = issue["node"]["title"]
    title = cleantitle(title)
    for comments in issue["node"]["comments"]["edges"]:
        #コメント内容
        comment = comments["node"]["bodyText"]
        #誰かいたか
        name = comments["node"]["author"]["login"]
        issuedic.append({"name":name,"comment":comment})
    fw = codecs.open(title+".json","w","utf-8")
    fw.write(json.dumps(issuedic,indent=3,ensure_ascii=False));
    fw.close()
