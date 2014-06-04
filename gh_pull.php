<?php
echo "CS10 Web hook Script <br />";
phpinfo();
echo 'User: ' . get_current_user() . '<br />';
$file = 'github.py';
$url = "http://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]";
fopen('file.txt', 'w');
$command = '/usr/local/bin/python ' . $file . ' "' . $url . '" 2>&1';
echo $file;
echo '<br />';
echo $url;
echo '<br />';
echo $command;
echo '<br />';
$py = exec('python3 test.py 2>&1');
echo $py;
echo '<br />';
echo exec('echo ${USER}');
echo '<br />';
$result = exec($command);
echo $result;

?>
