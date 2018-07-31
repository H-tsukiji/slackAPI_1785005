# -*- coding: utf-8 -*-

import codecs, json, sys, re

filename = sys.argv[1]
f = codecs.open(filename,"r","utf-8")
fjson = json.load(f)


def cleantitle(title):
    title = re.sub(' ','', title)
    title = re.sub('/','', title)
    return title

index_name = []
name_count = {}

for issue in fjson["issues"]["edges"]:
    for comments in issue["node"]["comments"]["edges"]:
        #誰かいたか
        name = comments["node"]["author"]["login"]
        if name not in index_name:
            index_name.append(name)
            name_count[name] = 1
        else:
            name_count[name] += 1

print(name_count)