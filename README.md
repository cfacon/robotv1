# robotv1

Ajouter le script de démarrage automatique

```
sudo nano /lib/systemd/system/autoStartServer.service
```


Ajouter ce code :
```
[Unit]
Description=MCHobby LCD Order Tracker
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python /home/pi/PrestaConsole/lcdordertrack.py > /home/pi/lcdordertrack.log 2>&1

[Install]
WantedBy=multi-user.target
```

met les bon droits
```
sudo chmod 644 /lib/systemd/system/myscript.service
```

Active le service
```
sudo systemctl daemon-reload
sudo systemctl enable myscript.service
```

Reboot pour tester
```
sudo reboot
```

Voir son etat :
```
sudo systemctl status lcdordertrack.service
```


Si besoin permet de démarrer le service après modification ou ajustement:
```
sudo systemctl start lcdordertrack.service
```
