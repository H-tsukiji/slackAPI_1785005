# -*- coding: utf-8 -*-

import codecs,sys,re,MeCab

filename = sys.argv[1]
f = codecs.open(filename, "r", "utf-8")

issue_comments = {
    "ktakano":"声が小さい\n行間が狭いところがある\n背景がわかりやすくなった\n「高い関心が持つ」とはちょっと違うと思う\n「今後の生活」はちょっと広い。今後、「英語を話すような局面」など。\nアイディアを説明した？\n上村システムとのDBの共有化\n発音記号があると有用。発音記号のDBはどこかで公開しているか調査して欲しい",
    "H-tsukiji":"実験するときはなのような形態でやるか決めましたか？",
    "unblee":"学習者にマッチした表現ってなんだ\nそろそろ実験の方法について言及しても良いかも\nセミナー中の口頭での議論のメモは一番上のコメントに反映させましょう！",
    "toC1421":"テンプレートに沿った箇条書きとかの方に直して綺麗にした方が絶対良いと思いました\n（行間バラバラになっていたり）\n「関連研究のこれとこれ」という言い方よりは「現在までの関連研究では～」という書き方にして、発表時には「[1]や[2]では～」という言い方にすれば良いと思いました\n・最後のスライドの写真が小さく・声も小さかったので何を説明しているか分かりませんでした",
    "misamatsuoka":"・今後の生活で使いそうな単語＝関心度が高い？\n・１文だったらどの単語が発言できなかったかがわかる？→技術的に辛そう"
}

def cleanInput(text):
    text = re.sub('\n', ' ', text)
    text = re.sub(r'[･%$&#:;＆。※↑↓→←：；＾？～￥「」（）()【】『』<>・_=|?［］]', ' ', text)
    text = re.sub(r'[@＠]\w+', ' ', text)
    text = re.sub(r'[0-9]', ' ', text)
    text = re.sub(r'[０-９]', ' ', text)
    text = re.sub('-', ' ', text)
    text = re.sub('/', ' ', text)
    text = re.sub('\n', ' ', text)
    text = re.sub('\r\n', ' ', text)
    text = re.sub('　', ' ', text)
    #text = re.sub('[ぁ-ん]', ' ', text)
    return text

def Mecab_parce(text):
    #形態素解析
    tagger = MeCab.Tagger('-Ochasen')
    pase_result = tagger.parseToNode(text)
    parselist = []
    while pase_result:
        #print ('%-10s \t %-s' % (pase_result.surface, pase_result.feature))
        tmp = pase_result.feature.split(",")    
        parselist.append({
            "word":pase_result.surface,
            "feature": tmp[0]
        })
        pase_result = pase_result.next
    return parselist




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

#イシューの形態素解析
comments_lists = []
for issue in issue_comments.values():
    tmplist = Mecab_parce(issue)
    comments_lists.extend(tmplist)

print(comments_lists)


