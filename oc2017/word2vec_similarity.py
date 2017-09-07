# -*- coding: utf-8 -*-

from gensim.models import word2vec
import sys,csv

model   = word2vec.Word2Vec.load('word2vec-gensim-model/word2vec.gensim.model')
results = model.most_similar(positive=sys.argv[1],negative="", topn=10)

try:
    # 書き込み UTF-8
    with open('word2vec_result.csv', 'w', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, lineterminator='\n')
        for i in results:
            writer.writerow([i[0],i[1]])

# 起こりそうな例外をキャッチ
except FileNotFoundError as e:
    print(e)
except csv.Error as e:
    print(e)