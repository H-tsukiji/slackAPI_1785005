# 修論プログラムのあれこれについて

## slackAPIの動かし方

トークンの取得する方法  
https://api.slack.com/docs/oauth-test-tokens

[Create token]をクリックすることで，Tokenが作成される。  

## channel idの取得
https://api.slack.com/methods/channels.list/test  
ここで送ると
{  
"id": "＊＊＊＊",  
"name": "チャンネル名",  
"is_channel": true  

idがチャンネルidとなる

## pythonプログラムで使用した拡張モジュール
拡張モジュールは基本的にpipにてインストールする事(たぶんすんなりいけるはず)  
- Slacker  
- matplotlib.pyplot  
- networkx  
- numpy  
- sudachipy  

sudachipyに関してはknowledgeレポジトリのwikiに記事があるためそちらを参照  
https://github.com/kait-takanolab/knowledge.wiki.git


## プログラムの説明
現段階ではユーザ役割における実験プログラムについて説明します。  


### get_slacklog.py  
API使って会話ログのJSONファイルを作成  
読み込んでいるもの：チャンネルID，SlackAPIトークン  
生成されるもの：[チャンネルID].json  
トークンのパスと指定チャンネルIDを変更する部分の例(下記)
```
token = codecs.open("../slackapi_token.txt", "r","utf-8")
c_name = 'C4W2RL2BA'
```

### slack_memberlist.py
slackにいるユーザ一覧の作成プログラム  
読み込んでいるもの：SlackAPIトークン  
生成されるもの：memberlist.json  

### slacklog_molding.py
各チャンネルのログを統合し、使いやすいように成形したcsvファイルの作成するプログラム  
読み込んでいるもの：Jsonフォルダパス，memberlist.json  
生成されるもの：slacklog.csv  
memberlist.jsonのパスとjsonファイルが詰まったフォルダパスを変更する部分の例(下記)  
```
files = glob.glob('logdata/json/20180925/*.json')
fm = codecs.open("memberlist.json","r","utf-8")
```

### extract_usermessage.py
slacklog.csvから各ユーザ毎に発言内容のtxtファイルを生成するプログラム  
入力する引数：slacklog.csvがあるパス  
生成されるもの："+row[0]+"_messages.txt(人数分できるから注意)  
生成したファイル保存する場所を変更する部分の例(下記)  
保存先に指定するフォルダはあらかじめ作成しておく事  
`userfile = open("logdata/20190214/"+row[0]+"_messages.txt","a",encoding="utf-8")`  
実行例:`python extract_usermessage.py slacklog.csv`

### get_reaction.py
Jsonファイルからslackのリアクションしてもらった人物とそのされた内容一覧を出力するプログラム  
読み込んでいるもの：Jsonフォルダパス，memberlist.json  
csvファイル(reaction_list.csv)を作成  
出力例  
User(リアクション送った人),touser(リアクションもらった人),text(対象の文章)  
t.kasai,takano,明日のチュラ研修生のプログラムです。  
memberlist.jsonのパスとjsonファイルが詰まったフォルダパスを変更する部分と生成されるファイル名とその場所の例(下記)  
```
files = glob.glob('logdata/json/20180925/*.json')
fm = codecs.open("memberlist.json","r","utf-8")
with open('count_reaction.csv', 'w', encoding="utf-8") as csvfile:
with open('reaction_list.csv', 'w', encoding="utf-8") as csvfile:
```

### get_thred.py
Jsonファイルからslackのスレッドで開始となった回数とスレッドで会話した回数一覧を出力するプログラム  
読み込んでいるもの：Jsonフォルダパス，SlackAPIトークン，memberlist.json  
生成されるもの：first_thread_user.csv(開始となった回数),  thread_message_countlist.csv(会話した回数)  
トークンのパスとmemberlist.jsonのパスとjsonファイルが詰まったフォルダパスを変更する部分と生成されるファイル名とその場所の例(下記)  
```
token = codecs.open("../slackapi_token.txt", "r","utf-8")
files = glob.glob('logdata/json/20180925/*.json')
fm = codecs.open("memberlist.json","r","utf-8")
with open('first_thread_user.csv', 'w', encoding="utf-8") as csvfile:
with open('thread_message_countlist.csv', 'w', encoding="utf-8") as csvfile:
```

### get_mention.py
だれがだれに何回リプライ(@で指定するメンション)をしたのかカウントするプログラム  
読み込んでいるもの：memberlist.json，txtフォルダパス  
生成されるもの：mention/mention_"+username+".csv  

### sudachi_wordcount.py
入力されたtxtファイルを分かち書きして使用単語頻度一覧を出力するプログラム  
入力する引数：対象のtxtファイルパス  
生成されるもの：filename+'.csv'  

### userrole_experiment.py
実験プログラム  
読み込んでいるもの：  
- reaction_list.csv
- thread_message_countlist.csv
- first_thread_user.csv
- jyodoshi_count.csv
- memberlist.json
- rep_"+username+".csvを詰め込んだフォルダ  

入力する引数：  sudachi_wordcount.pyで生成したファイルが詰まったフォルダパス  
出力されるもの：各ユーザ役割スコアと内容類似度  


## 実験方法

### ユーザ役割の実験方法

#### 1. 実験で使用する会話ログのデータセット作成方式  
プログラムにて生成させるjsonファイル，csvファイル，txtファイルはlogdataフォルダ内に配置する事．  

get_slacklog.pyで作成されたjsonファイルはlogdataのjsonフォルダ内にて日付など実験データの取得時がわかりやすいものにする．  
例：2019/2/15に取得した場合に「20190215」とかのファイル内に取得したjsonファイルを突っ込んでおく．  
生成したjsonファイルの名前についてはチャンネルIDを自動で振られるけど自分がわかるように変更してもよい(日本語はNG)  



距離の計算はエクセルで計算してね
