#coding: utf-8

import socket
import json

# Récupération des informations sur le serveur stocké dans le .json (Ip et le Port)
with open('settings.json') as fichier: 
    settings = json.load(fichier)


###############################################
##                 CLIENT                    ##
###############################################

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((settings["ip"],settings["port"])) # Connexion au serveur


while True:
    print("Message à envoyer au serveur:")
    data = input(">> ")
    data = data.encode("utf8") # On encode le message
    s.sendall(data) # On envoie le message au serveur sous sa version encodé

    # Le Serveur renvoit quelque chose

    dataServeur =''
    dataServeur = s.recv(1024)
    dataServeur = dataServeur.decode("utf8") # On le décode car encodé coté serveur avant l'envoi
    if dataServeur == "break":
        break
    print(dataServeur) # On affiche le contenu de ce que nous avons reçu