<?php
// echo "CS10 Web hook Script <br />";
// phpinfo();
// echo 'User: ' . get_current_user() . '<br />';
// $url = "http://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]";
// $command = '/usr/local/bin/python ' . $file . ' "' . $url . '" 2>&1';
// echo $file;
// echo '<br />';
// echo $url;
// echo '<br />';
// echo $command;
// echo '<br />';
// $py = exec('python3 test.py 2>&1');
// echo $py;
// echo '<br />';
// echo exec('echo ${USER}');
// echo '<br />';
$dir = '/home/ff/cs10/github/';
$log = $dir . 'php_log.txt';
$file = $dir . 'github.py';
$sep = '
==================================================
';
$event = $_POST['X-Github-Event'];
// $postdata = $HTTP_RAW_POST_DATA;
// $var = putenv('var=TEST');
// echo $var;
// echo '<br />';
$command = '/usr/sww/bin/python3 ' . $file . ' \'' . $HTTP_RAW_POST_DATA . '\' \'' . $event . '\' 2>&1';
// echo $command;
file_put_contents($log, $sep, FILE_APPEND);
file_put_contents($log, 'WEB HOOK EXEC @ ' . date("Y-m-d H:i:s") . '
', FILE_APPEND);
file_put_contents($log, 'WEB HOOK EVENT - ' . $event . '
', FILE_APPEND);
// echo '<br />';
$result = exec($command);
file_put_contents($log, 'RESULT:  ' . $result, FILE_APPEND);
file_put_contents($log, $sep, FILE_APPEND);
// echo $result;
?>
