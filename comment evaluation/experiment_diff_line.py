# -*- coding: utf-8 -*-
import codecs,sys,re,MeCab,json,csv
import numpy as np

def cleanInput(text):
    text = re.sub(r'\f', '', text)
    #text = re.sub(r'[@＠]\w+', ' ', text)
    #text = re.sub('[･%$&#:;＆。※↑↓→←：；＾？～￥「」/-（）()【】『』<>・_=|?［］\"\']','', text)
    text = re.sub(r'[0-9]', '', text)
    #text = re.sub(r'[０-９]', '', text)
    text = re.sub(r'\r\n', '', text)
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
        if tmp[0] == '助動詞':
            pase_result = pase_result.next
            continue
        if tmp[0] == 'BOS/EOS':
            pase_result = pase_result.next
            continue
        if tmp[1] == "サ変接続" and tmp[6] == "*":
            pase_result = pase_result.next
            continue
        parselist.append({
            "word":pase_result.surface,
            "feature": tmp[0]
        })
        pase_result = pase_result.next
    return parselist

#頻度算出
def count_word(wordlist,index):
    count_list = {}
    for word in index:
        count_list[word] = 0

    for word in wordlist:
        term = word["word"]
        count_list[term] += 1
    return count_list

def cos_sim_matrix(matrix):
    """
    item-feature 行列が与えられた際に
    item 間コサイン類似度行列を求める関数
    """
    d = matrix @ matrix.T  # item-vector 同士の内積を要素とする行列
    # コサイン類似度の分母に入れるための、各 item-vector の大きさの平方根
    norm = (matrix * matrix).sum(axis=1, keepdims=True) ** .5
    # それぞれの item の大きさの平方根で割っている
    return d / norm / norm.T


diff_filename = sys.argv[1]
f = codecs.open(diff_filename, "r", "utf-8")

issue_filename = sys.argv[2]
fj = codecs.open(issue_filename,"r","utf-8")
issue_comments = json.load(fj)

#print(issue_comments)

#txtから文章を格納
diff_text = []
for line in f:
    if re.search("^\+",line):
        line = re.sub("\+","",line)
        #diff_text += line
    else:
        continue
    line = cleanInput(line)
    diff_text.append(line)
l_odd = [i for i in diff_text if (not i == "\r\n") and (not i == "")]
diff_text.clear()
diff_text = l_odd
#print(diff_text)

#差分文章の形態素解析
diff_list = []
for d_line in diff_text:
    diff_list.append(Mecab_parce(d_line))
#print(diff_list)

#イシューの形態素解析
comments_lists = []
for issue in issue_comments:
    tmp_list = Mecab_parce(issue["comment"])
    comments_lists.append({"name":issue["name"],"parse":tmp_list})
#print(comments_lists)


#コメントの語句を登録
comment_index= []
for comment in comments_lists:
    for word in comment['parse']:
        term = word["word"]
        if term not in comment_index:
            comment_index.append(term)
        else:
            continue
#print(comment_index)

with open('saito07.csv', 'w') as f:
    writer = csv.writer(f)

    #1行づつ結果見てく
    for i, d_line in enumerate(diff_list):
        term_index = []
        term_index.extend(comment_index)
        #差分の語句を登録
        for word in d_line:
            term = word["word"]
            if term not in term_index:
                term_index.append(term)
            else:
                continue
        #print(term_index)

        #差分の頻度
        diff_freq = count_word(d_line,term_index)
        #ベクトル化
        diff_vec = []
        for num in diff_freq.values():
            diff_vec.append(num)

        #こめんとの頻度
        comments_freq = []
        for comment in comments_lists:
            #print(comment['name'])
            tmp_freq = count_word(comment['parse'],term_index)
            comments_freq.append({"name":comment['name'],"freq":tmp_freq}) 
        #ベクトル化
        comments_vec = []
        for comment in comments_freq:
            tmp_vec = []
            for num in comment["freq"].values():
                tmp_vec.append(num)
            comments_vec.append({"name":comment['name'],"vec":tmp_vec})
        #print(comments_vec)

        #対応文書
        #print(diff_text[i])
        tmp = []
        tmp.append(i)
        tmp.append(diff_text[i])
        #writer.writerow(tmp)

        #相関係数
        for comment in comments_vec:
            #print(comment['name'])
            #print(np.corrcoef(diff_vec, comment['vec'])[0, 1])
            value_p =str(np.corrcoef(diff_vec, comment['vec'])[0, 1])

        #コサイン類似度
        cos_list = []
        cos_list.append(diff_vec)
        for comment in comments_vec:
            cos_list.append(comment['vec'])
        data_list = np.array(cos_list)
        data_list = data_list.astype(np.int)
        result = cos_sim_matrix(data_list)
        cosresult = result[0]
        #print(result[0])
        tmp.extend(cosresult)
        writer.writerow(tmp)        
        #writer.writerow(cosresult)
        #np.savetxt('result_cos.csv', result, delimiter=',')

f.close()

