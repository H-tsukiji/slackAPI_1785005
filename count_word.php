<?php

$dir = new DirectoryIterator($argv[1]);

foreach($dir as $f){
    if($f -> isFile()){
        $filepath = $f -> getPathName();
        $filename = $f -> getFileName();
        $result_word = count_wordindex($filepath);

        //拡張子抜きのパスとファイル名の入手
        //$filename = preg_replace('|^[a-z]+\\|', "", $filename);
        $filename = preg_replace('|\.+[a-z]+$|',"",$filename);
        //jsonファイルの作成
        $fp = fopen('txt/'.$filename.'.json',"w");
        fwrite($fp, json_encode($result_word,JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT));
        fclose($fp);
        unset($result_word);
    }
}

//単語集計するプログラム引数はファイル返り血は配列
function count_wordindex($fn){
    $data = @file($fn);
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
    return $word_list;
}

?>