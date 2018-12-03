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

csvdata = []

with open("jyodousi.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        csvdata.append(row)

#print(csvdata)

def search_meaning(text):
    mean = []
    for word in csvdata:
        if text == word[0]:
            mean.append(word[1])
    return mean

word_list = {}
word_index = []
text = []

if __name__ == '__main__':    
    mode = tokenizer.Tokenizer.SplitMode.C
    for line in lines:
        line = re.sub(r"(<.+>)","",line)
        for i in [m.surface() for m in tokenizer_obj.tokenize(mode, line)]:
            #print(i)
            try:
                result = tokenizer_obj.tokenize(mode, i)[0].normalized_form()
            except IndexError:
                continue
            part_list = tokenizer_obj.tokenize(mode, result)[0].part_of_speech()

            if (part_list[0] == '助動詞'):
                #print(result,part_list)
                text.append(search_meaning(result))
                print(text)
