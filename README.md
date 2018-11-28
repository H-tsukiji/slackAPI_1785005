# SlackAPI

私がSlackAPIを動かしてみる為にいろいろと試行錯誤するレポジトリです


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

## ユーザ名とユーザidの紐づけ
memberlist.json  
idとユーザ名がセットである。  
これを作成するプログラムはslack_userlist.py  
jsonファイル使いまわしてね

## ログを取る方法
slackからログをjson形式で取得するプログラム  
slacker_log.py  

「slacker_log.py」で取得したjsonファイルから会話ログのcsvに直す  
log_analysis.py  

「log_analysis.py」で作成した各チャンネルの会話ログのcsvファイルより各ユーザのメッセージ毎にテキストファイルを追加するプログラム(追記のa読み込みに注意)  
user_message.py  

「user_message.py」で作成したtxtファイルを構文解析して名詞系の語句頻度をcsvで出力するプログラム  
sudachi.py  

csvファイル「log_report_channel」に名前内容時間を書き込む  

## csvファイルの出力
log_analysis.py  
csvファイルにユーザ名、内容、タイムスタンプを出力するプログラム

### ここには備忘録としてリンクなど張りたい

http://nuxx.noob.jp/archives/135  
http://qiita.com/Yinaura/items/bd28c7b9ef614696fb7e
