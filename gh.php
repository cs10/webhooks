<?php
// Location of hooks data directory
$dir = '/home/ff/cs10/github/';
// System python command (python isn't in PHP user path)
$python = '/usr/sww/bin/python3';
$log = $dir . 'php_log.txt';
// Script to execute
$file = $dir . 'github.py';
// Logging shortcuts
$nl   = '
';
$sep = '==================================================';
$event = $_POST['X-Github-Event'];
// Command to run
// MAKE SURE TO INCLUDE '' AROUND THE POST DATA
// Command Captures stderr and stdout
$command = $python . ' ' . $file . ' \'' . $HTTP_RAW_POST_DATA . '\' \'' . $event . '\' 2>&1';
// Logging stuffs
file_put_contents($log, $nl . $sep . $nl, FILE_APPEND);
file_put_contents($log, 'WEB HOOK EXEC  @ ' . date("Y-m-d H:i:s") . $nl, FILE_APPEND);
// TODO: Log Repo Name, Account
file_put_contents($log, 'WEB HOOK EVENT - ' . $event . $nl, FILE_APPEND);
// Run command, save output and log it.
$result = exec($command);
file_put_contents($log, 'RESULT:  ' . $result, FILE_APPEND);
file_put_contents($log, $nl . $sep . $nl, FILE_APPEND);
// Send some data back about the results
// Mostly helpful for debugging on GH
// TODO: Send appropriate status code
HttpResponse::status(200);
HttpResponse::setContentType('text/xml');
HttpResponse::setData('WEB HOOK EXEC FINISHED:' . $nl . $result);
HttpResponse::send();

?>
