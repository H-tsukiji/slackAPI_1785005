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
slacker_log.py  
必要な情報  
チャンネルid  
現状オブジェクトで帰っているので、配列に整理するかなんかする必要がありそう・・・？  
.bodyを付与することでできた。  
csvファイル「log_report_channel」に名前内容時間を書き込む  

## csvファイルの出力
log_analysis.py  
csvファイルにユーザ名、内容、タイムスタンプを出力するプログラム

### ここには備忘録としてリンクなど張りたい

http://nuxx.noob.jp/archives/135  
http://qiita.com/Yinaura/items/bd28c7b9ef614696fb7e

