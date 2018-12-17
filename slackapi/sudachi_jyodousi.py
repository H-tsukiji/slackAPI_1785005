# -*- coding: utf-8 -*-
import json,sys,codecs,csv,re,glob,os
from sudachipy import tokenizer
from sudachipy import dictionary
from sudachipy import config

#辞書読み込み？
with open(config.SETTINGFILE, "r", encoding="utf-8") as f:
    settings = json.load(f)
tokenizer_obj = dictionary.Dictionary(settings).create()


files = []
files = glob.glob('20180925/*.txt')

csvdata = []
with open("jyodousi.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        csvdata.append(row)

def search_meaning(text):
    mean = []
    for word in csvdata:
        if text == word[0]:
            mean.append(word[1])
    return mean

if __name__ == '__main__':    
    jyodoshi = []
    for file in files:      
        word_list = []
        total_count = 0
        inputfilename = file
        file = codecs.open(inputfilename, "r","utf-8")
        lines = file.readlines()
        username = os.path.basename(inputfilename)
        username = re.sub('_messages.txt','',username)

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
                    total_count += 1
                    text = []
                    text.append(result)
                    text.extend(search_meaning(result))
                    #print(text)
                    word_list.append(text)
        
        order_count = 0
        respect_count = 0
        for word in word_list:
            if ("使役" in word):
                order_count += 1
            '''
            elif ("尊敬" in word) or ("丁寧" in word):
                respect_count += 1
            '''
        # print('order_count:', order_count)
        # print('total      :', total_count)
        # print('rate       :', order_count/total_count)
        jyodoshi.append([username, order_count, total_count, order_count/total_count])

    try:
        with open("jyodoshi_count.csv", 'w', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, lineterminator='\n')
            writer.writerow(['user', 'order_count', 'total_count', 'rate'])
            for i in jyodoshi:
                writer.writerow([i[0], i[1], i[2], i[3]])
    # 起こりそうな例外をキャッチ
    except FileNotFoundError as e:
        print(e)
    except csv.Error as e:
        print(e)