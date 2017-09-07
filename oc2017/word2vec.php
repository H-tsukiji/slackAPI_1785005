<?php

#ajax動作テストhelloを返す

$word = $_POST["word"];
$word = mb_convert_encoding($word, "SJIS");

exec("python word2vec_similarity.py ".$word);

$csv_data = file_get_contents("word2vec_result.csv");

$csv_data = str_replace("\r\n","\n",$csv_data);
$csv_data = str_replace(","," ",$csv_data);
$value_data = explode("\n",$csv_data);

$data = array();
$count = 0;
foreach($value_data as $value){
    $parce = explode(" ",$value);
    if($parce[0] === ""){
        continue;
    }
    else{
        $data[] = array('word' => $parce[0], 'score' => $parce[1]);
    }
}

print json_encode($data);

?>