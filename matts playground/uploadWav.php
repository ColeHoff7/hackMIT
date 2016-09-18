<?php
// requires php5
define('UPLOAD_DIR', 'uploads/');
$img = $_POST['wavBase64'];
$img = str_replace('data:audio/wav;base64,', '', $img);
$img = str_replace(' ', '+', $img);
$data = base64_decode($img);
$i = 0;
while(file_exists($i.'.wav')){
	$i++;
}
$file = $i . '.wav';
$success = file_put_contents($file, $data);
print $success ? $file : 'Unable to save the file.';
?> 