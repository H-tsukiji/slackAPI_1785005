# -*- coding: utf-8 -*-
import codecs,sys,re,MeCab,json

def cleanInput(text):
    text = re.sub('\n', ' ', text)
    text = re.sub(r'[･%$&#:;＆。※↑↓→←：；＾？～￥「」/-（）()【】『』<>・_=|?［］\[\]\"\']', ' ', text)
    text = re.sub(r'[@＠]\w+', ' ', text)
    text = re.sub(r'[0-9]', ' ', text)
    text = re.sub(r'[０-９]', ' ', text)
    text = re.sub('\r\n', ' ', text)
    #text = re.sub('[ぁ-ん]', ' ', text)
    return text

def Mecab_parce(text):
    #形態素解析
    tagger = MeCab.Tagger('-Ochasen')
    tagger.parse('')
    pase_result = tagger.parseToNode(text)
    parselist = []
    while pase_result:
        #print ('%-10s \t %-s' % (pase_result.surface, pase_result.feature))
        tmp = pase_result.feature.split(",")  
        if tmp[0] == '記号':
            pase_result = pase_result.next
            continue
        if tmp[0] == '助詞':
            pase_result = pase_result.next
            continue
        if tmp[0] == 'BOS/EOS':
            pase_result = pase_result.next
            continue
        parselist.append({
            "word":pase_result.surface,
            "feature": tmp[0]
        })
        pase_result = pase_result.next
    return parselist


diff_filename = sys.argv[1]
f = codecs.open(diff_filename, "r", "utf-8")

issue_filename = sys.argv[2]
fj = codecs.open(issue_filename,"r","utf-8")
issue_comments = json.load(fj)

#print(issue_comments)

#txtから文章を格納
diff_text = ""
for line in f:
    if re.search("^\+",line):
        line = re.sub("\+","",line)
        diff_text += line
    else:
        continue
#print(diff_text)

#差分文章の形態素解析
diff_list = Mecab_parce(diff_text)
#print(diff_list)

#イシューの形態素解析
comments_lists = []
for issue in issue_comments:
    tmp_list = Mecab_parce(issue["comment"])
    comments_lists.append({"name":issue["name"],"parse":tmp_list})

print(comments_lists)