# Daily Messages

## Description

Crée un serveur web.
Tout les jours, un message différent est disponible sur le site.

## Lancer l'application

Avec ou sans environnement virtuel, il suffit d'installer les dépendances et de lancer le script.

```shell
pip install -r requirements.txt

python daily_messages.py
```

## Deploiement

Mettre tout le dossier dans /daily-message.

Installer les dépendances
````
pip install -r /daily-message/requirements.txt
```

Rendre le script exécutable.

```shell
chmod +x /daily-message/start.sh
```

Ajouter le script en service.

```shell
sudo ln -s /daily-message/daily-message.service /etc/systemd/system/daily-message.service
```