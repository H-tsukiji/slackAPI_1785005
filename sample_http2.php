<?php
require_once 'HTTP/Request2.php';
$url = 'http://allabout.co.jp';
$http_request = new HTTP_Request2();
$http_request->setUrl($url);
$http_request->setMethod(HTTP_Request2::METHOD_GET);
$ret = $http_request->send();
var_dump($ret);



?>
