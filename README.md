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

### slacklog_molding.py
各チャンネルのログを統合し、使いやすいように成形したcsvファイルの作成するプログラム  
読み込んでいるもの：Jsonフォルダパス，memberlist.json  
生成されるもの：slacklog.csv  

### extract_usermessage.py
slacklog.csvから各ユーザ毎に発言内容のtxtファイルを生成するプログラム  
入力する引数：slacklog.csvがあるパス  
生成されるもの："+row[0]+"_messages.txt(人数分できるから注意)  

### slack_memberlist.py
slackにいるユーザ一覧の作成プログラム  
読み込んでいるもの：SlackAPIトークン  
生成されるもの：memberlist.json  

### get_reaction.py
Jsonファイルからslackのリアクションしてもらった人物とそのされた内容一覧を出力するプログラム  
読み込んでいるもの：Jsonフォルダパス，memberlist.json  
csvファイル(reaction_list.csv)を作成  
出力例  
User(リアクション送った人),touser(リアクションもらった人),text(対象の文章)  
t.kasai,takano,明日のチュラ研修生のプログラムです。  

### get_thred.py
Jsonファイルからslackのスレッドで開始となった回数とスレッドで会話した回数一覧を出力するプログラム  
読み込んでいるもの：Jsonフォルダパス，SlackAPIトークン，memberlist.json  
生成されるもの：first_thread_user.csv(開始となった回数),  thread_message_countlist.csv(会話した回数)  

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

距離の計算はエクセルで計算してね
