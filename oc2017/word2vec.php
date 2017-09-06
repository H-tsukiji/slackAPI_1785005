<?php

#ajax動作テストhelloを返す

$word = $_POST["word"];
$word = mb_convert_encoding($word, "SJIS");

exec("python word2vec_similarity.py ".$word);

#これはあとでやるたぶんコロンが悪い
#$data = @file("word2vec_result.csv");
$data = file_get_contents("word2vec_result.csv");

print json_encode("$data");

?>