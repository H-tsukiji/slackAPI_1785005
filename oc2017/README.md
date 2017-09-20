# オープンキャンパスのプログラム  

## 必要な環境
python3  
php5.6  
Apache  
pythonではword2vecを動かすために以下のパッケージのインストールをしてください。  
・gensim  
・numpy  
・scipy  
パッケージインストールの詳しい説明はword2vecのフォルダ内にあるREADMEを参照してください。

## ディレクトリ構成
・bootstrap：デザインシート置き場  
・jqcloud：タグクラウド作成プログラム  
・word2vec-gensim-model：word2vecの学習モデル  

## プログラム説明(概要)
index.html：フロント。jQueryを読み込んでいるのでインターネットに接続された環境で行ってください。もしかしたら、文字コードが化けているかも。  
word2vec.php：index.htmlで得たキーワードを基にword2vecを用いるpythonプログラムを起動し結果を正規化して返すプログラム。OS環境によって調整する必要があるため注意する事  
jqcloud.js：index.htmlで取得した単語スコアを基にタグクラウドを作成するプログラム  
word2vec_similarity.py：モデルを基に指定されたキーワードのベクトルと近いものを抽出するプログラム  
word2vec_train.py：指定されたデータを基に学習モデルを作成するプログラム。今回の用途では使用しないが、念のため置いておく。  
word2vec_result.csv：word2vec\_similarity.pyで出た結果が書かれているデータ保存用
