import MeCab,re

text = '日本語の自然言語処理は本当にしんどい。'

#分かち書き
tagger = MeCab.Tagger("-Owakati")        
result = tagger.parse(text)
#print(result)

listresult = result.split(" ")
#print(listresult)


#形態素解析
tagger = MeCab.Tagger('-Ochasen')
result = tagger.parseToNode(text)

parselist = []
while result:
    print ('%-10s \t %-s' % (result.surface, result.feature))

    tmp = result.feature.split(",")    
    parselist.append({
        "word":result.surface,
        "feature": tmp[0]
    })
    result = result.next

print(parselist)