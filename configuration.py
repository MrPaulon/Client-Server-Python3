#coding: utf-8

import json

ip = input("Quelle est l'ip que vous voulez donnez à votre serveur ? (Recommendé: 127.0.0.1):\n>> ")
port = int(input("Quel port voulez vous attribuez à votre serveur ? (Recommandé: 12086)\n>> "))

settings = {
    "ip": ip,
    "port": port
}

with open("settings.json", 'w') as fichier:
    json.dump(settings, fichier)
