<?php
// Location of hooks data directory
$dir = '/home/ff/cs10/github/';
// System python command (python isn't in PHP user path)
$python = '/usr/sww/bin/python3';
$logFile = $dir . 'php_log.txt';
// Script to execute
$file = $dir . 'github.py';
// Logging shortcuts
$nl   = '
';
$sep = '==================================================';
$event = $_POST['X-GitHub-Event']; // note capitalization!
// Command to run
// MAKE SURE TO ENCODE THE POST DATA! -- put it in '' as well.
// Command Captures stderr and stdout
$command = $python . ' ' . $file . ' \'' . rawurlencode($HTTP_RAW_POST_DATA) . '\' \'' . $event . '\' 2>&1';
// Pre-Exec Logging stuffs
// Log to File and Echo for GH output.
$logData = $nl . $sep . $nl;
$logData = $logData . 'WEB HOOK EXEC  @ ' . date("Y-m-d H:i:s") . $nl;
$logData = $logData . 'WEB HOOK EVENT - ' . $event . $nl;
// TODO: Log Repo Name, Account
file_put_contents($logFile, $logData, FILE_APPEND);
// TEST -- Log Python User to GH
$py = exec($python . ' -c \'import os; print(os.system("whoami"))\'');
echo($py);
echo($logData);
var_dump($_POST);
echo('COMMAND:  ' . $nl . $command . $nl . $sep . $nl);
// Run command, save output and log it.
$result = exec($command);
// Send some data back about the results
echo('RESULT:  ' . $result);
file_put_contents($logFile, 'RESULT:  ' . $result, FILE_APPEND);
file_put_contents($logFile, $nl . $sep . $nl, FILE_APPEND);

?>
