import csv, sys, MeCab, re

#対象ファイルの取得および分かち書きの設定
inputfilename = sys.argv[1]
file = open(inputfilename, 'r', encoding="utf-8")
output = open(inputfilename+"_wakati.txt", 'w', encoding="utf-8")
tagger = MeCab.Tagger("-Owakati")
csvdata = csv.reader(file)

#1行づつ読み込みノイズとなるような記号とひらがなを排除
def cleanInput(text):
    text = re.sub('\n', ' ', text)
    text = re.sub(r'[.,･%$&#:;＆。※↑↓→←、．，：；＾？～￥「」（）()【】『』<>・_=|?［］\[\]\"\']', ' ', text)
    text = re.sub(r'[@＠]\w+', ' ', text)
    text = re.sub(r'[0-9]', ' ', text)
    text = re.sub(r'[０-９]', ' ', text)
    text = re.sub('-', ' ', text)
    text = re.sub('/', ' ', text)
    text = re.sub('　', ' ', text)
    text = re.sub('[ぁ-ん]', ' ', text)
    return text

#txtファイルの作成
for row in csvdata:
    w_text = cleanInput(row[1])
    w_text = tagger.parse(w_text)
    output.write(w_text+"\n")

output.close()
