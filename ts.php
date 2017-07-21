<?php

$dir = new DirectoryIterator($argv[1]);

foreach($dir as $f){
    if($f -> isFile()){
        $filename = $f -> getPathName();

        print($filename);
        print("\n");
    }
}


?>