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

jyodousi_file = open("jyodousi.csv", 'r', encoding="utf-8")
csvdata = csv.reader(jyodousi_file)

print(csvdata)



def search_meaning(text):
    global mean = []
    for word in csvdata:
        if (text in word[0]) == True:
            mean = word[1]
    if not mean:
        mean = "null"
    return mean


word_list = {}
word_index = []

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
                print(result,part_list)
                text = search_meaning(result)
                print(text)    
