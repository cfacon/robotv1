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
ExecStart=/usr/bin/python /home/pi/robotRelease/robotv1/autoPull.py > /home/pi/autoStartServer.log 2 > &1

[Install]
WantedBy=multi-user.target
```

met les bon droits
```
sudo chmod 644 /lib/systemd/system/autoStartServer.service
```

Active le service
```
sudo systemctl daemon-reload
sudo systemctl enable autoStartServer.service
```

Reboot pour tester
```
sudo reboot
```

Voir son etat :
```
sudo systemctl status autoStartServer.service
```


Si besoin permet de démarrer le service après modification ou ajustement:
```
sudo systemctl start autoStartServer.service
```
