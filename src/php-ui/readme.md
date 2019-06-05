Auf dem RPi läuft Apache-Http auf Port 80 und PHP ist installiert. Das Wurzelverzichnis ist `/var/www/html` und darunter haben wir folgende Verzeichnisse über symbolische Links eingehangen:

```
/var/www/html/
    index.html
    php/        => /home/pi/php/
/home/pi/php/
    hello.php
    pico/       => /home/pi/pico/src/php-ui/
/home/pi/pico/src/php-ui/
    lucky-luke-ergebnisse.php    <= http://localhost/php/pico/lucky-luke-ergebnisse.php
```

