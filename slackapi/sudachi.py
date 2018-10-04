# -*- coding: utf-8 -*-
import json,sys,codecs,csv,re
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
filename = re.sub("\.[a-z]+","",inputfilename)

word_list = {}
word_index = []

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
            if part_list[1] == '数詞':
                continue
            if result not in word_index:
                word_index.append(result)
                word_list[result] = 1
            else:
                word_list[result] += 1

try:
    with open(filename+'.csv', 'w', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, lineterminator='\n')
        for key in word_list:
            writer.writerow([key, word_list[key]])
# 起こりそうな例外をキャッチ
except FileNotFoundError as e:
    print(e)
except csv.Error as e:
    print(e)
