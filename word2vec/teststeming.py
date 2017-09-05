import nltk,sys
english_stemmer = nltk.stem.SnowballStemmer('english')

print(english_stemmer.stem(sys.argv[1]))
