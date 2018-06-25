# -*- coding: utf-8 -*-

import codecs,sys,re

filename = sys.argv[1]
f = codecs.open(filename, "r", "utf-8")


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
    text = re.sub(r'\f', ' ', text)
    text = re.sub('\v', ' ', text)
    text = re.sub('\r', ' ', text)
    #text = re.sub('[ぁ-ん]', ' ', text)
    return text


diff_text = ""
for line in f:
    if re.search("^\+",line):
        line = re.sub("\+","",line)
        cleanInput(line)
        #print(line)
        diff_text += line
    else:
        continue


print(diff_text)


fout_utf = codecs.open("test.txt", "w", "utf-8")
for row in diff_text:
    fout_utf.write(row)
fout_utf.close()

issue_comments = {
    "ktakano":"声が小さい\n行間が狭いところがある\n背景がわかりやすくなった\n「高い関心が持つ」とはちょっと違うと思う\n「今後の生活」はちょっと広い。今後、「英語を話すような局面」など。\nアイディアを説明した？\n上村システムとのDBの共有化\n発音記号があると有用。発音記号のDBはどこかで公開しているか調査して欲しい",
    "H-tsukiji":"実験するときはなのような形態でやるか決めましたか？",
    "unblee":"学習者にマッチした表現ってなんだ\nそろそろ実験の方法について言及しても良いかも\nセミナー中の口頭での議論のメモは一番上のコメントに反映させましょう！",
    "toC1421":"テンプレートに沿った箇条書きとかの方に直して綺麗にした方が絶対良いと思いました\n（行間バラバラになっていたり）\n「関連研究のこれとこれ」という言い方よりは「現在までの関連研究では～」という書き方にして、発表時には「[1]や[2]では～」という言い方にすれば良いと思いました\n・最後のスライドの写真が小さく・声も小さかったので何を説明しているか分かりませんでした",
    "misamatsuoka":"・今後の生活で使いそうな単語＝関心度が高い？\n・１文だったらどの単語が発言できなかったかがわかる？→技術的に辛そう"
}
