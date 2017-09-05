<?php

$ai = $argv[1];

exec("mecab -Owakati ".$ai."",$result);

var_dump($result);