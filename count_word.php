<?php

$filename = $argv[1];
$data = @file($filename);

//拡張子抜きのパスとファイル名の入手
$filename = preg_replace('|\.+[a-z]+|',"",$filename);

$word_list_index = array(); //登録された単語を入れる。ここで既に登録されたかを確認する
$word_list = array();   //既に登録された単語の回数を入れていく

//配列ごとに処理
foreach ($data as $value) {
    $word_set = explode(" " , $value); 
    
    foreach($word_set as $value){
        $key = array_search($value,$word_list_index);
        if($key === false){  //新出単語のとき
            $word_list[] = array('num' => 1 ,'word' => $value );   //登録
            $word_list_index[] = $value;   //インデックスに登録
        }
        else {   //既に単語がある
            $word_list[$key]['num'] += 1;    
        }
    }
}

unset($word_list_index);    //インデックスの破棄

//出現回数順にソート
$num = array();
foreach ($word_list as $v) {
    $num[] = $v['num'];
}
array_multisort($num, SORT_DESC, SORT_NUMERIC, $word_list);

//jsonファイルの作成
$fp = fopen(''.$filename.'_json',"w");
fwrite($fp, json_encode($word_list,JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT));
fclose($fp);

unset($word_list);



?>