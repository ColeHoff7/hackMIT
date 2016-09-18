<?php
//requires php5

define('UPLOAD_DIR', 'uploads/');
$img = file_get_contents('php://input'); 
$img = str_replace('data:audio/wav;base64,', '', $img);
$img = str_replace(' ', '+', $img);
$data = base64_decode($img);
$i = 0;
while(file_exists('audio/'.$i.'.wav')){
	$i++;
}
$file = 'audio/'.$i . '.wav';
$success = file_put_contents($file, $data);
//print $success ? $file : 'Unable to save the file.';


$command = escapeshellcmd('python conversation.py '.$file);
$output = shell_exec($command);
print $output;


?> 