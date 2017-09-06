# -*- coding: utf-8 -*-

from gensim.models import word2vec
import sys

model   = word2vec.Word2Vec.load('word2vec-gensim-model/word2vec.gensim.model')
results = model.most_similar(positive=sys.argv[1],negative="", topn=10)

for result in results:
    print(result[0], '\t', result[1])

#print(model[sys.argv[1]])