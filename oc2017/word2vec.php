<?php

#ajax動作テストhelloを返す
$word = $_POST["word"];

$data = "hello";

print json_encode("$data");

?>