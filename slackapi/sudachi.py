# -*- coding: utf-8 -*-
import json,sys,codecs
from sudachipy import tokenizer
from sudachipy import dictionary
from sudachipy import config


#辞書読み込み？
with open(config.SETTINGFILE, "r", encoding="utf-8") as f:
    settings = json.load(f)
tokenizer_obj = dictionary.Dictionary(settings).create()

inputfilename = sys.argv[1]
file = codecs.open(inputfilename, "r","utf-8")
lines = file.readlines()

mode = tokenizer.Tokenizer.SplitMode.C
for line in lines:
    for i in [m.surface() for m in tokenizer_obj.tokenize(mode, line)]:
        #print(i)
        try:
            result = tokenizer_obj.tokenize(mode, i)[0].normalized_form()
        except IndexError:
            continue
        part_list = tokenizer_obj.tokenize(mode, result)[0].part_of_speech()
        if (part_list[0] == '名詞') or (part_list[0] == '動詞'):
            print(result)
            print(part_list)