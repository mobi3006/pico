<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="1" >
</head>
<body>
<h1>Lucky Luke Ergebnisse - Challenge 2019</h1>
<h2>Teilnehmer</h2>
<?php
    $myfile=fopen("/home/pi/pico/daten/spieler.xml", "r");
    while(!feof($myfile)) {
        echo fgets($myfile) . "<br>";
    }
    fclose($myfile);    
?>
<h2>Ergebnisse</h2>
<?php
    $myfile=fopen("/home/pi/pico/daten/ergebnisse.xml", "r");
    while(!feof($myfile)) {
        echo fgets($myfile) . "<br>";
    }
    fclose($myfile);    
?>
</body>
</html>
