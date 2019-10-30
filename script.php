<?php
$to = "faltushiv9@gmail.com";
$subject = "My subject";
$txt = "Hello world!";
$headers = "From: faltushiv9@gmail.com" . "\r\n" .
"CC: somebodyelse@example.com";

mail($to,$subject,$txt,$headers);
?>
