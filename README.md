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

Mettre tout le dossier dans /daily-messages.

Rendre le script exécutable.

```shell
chmod +x /daily-messages/start.sh
```

Ajouter le script en service.

```shell
sudo ln -s /daily-messages/daily-messages.service /etc/systemd/system/daily-messages.service
```