<?php
echo "CS10 Web hook Script <br />";
phpinfo();
echo 'User: ' . get_current_user() . '<br />';
$file = 'github.py';
$url = "//$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]";
$command = 'python ' . $file . ' "' . $url . '" 2>&1';
echo $file;
echo '<br />';
echo $url;
echo '<br />';
echo $command;
echo '<br />';
$result = exec($command);
echo $result;

?>