#coding: utf-8

import socket
import threading
import json


# Récupération des informations sur le serveur stocké dans le .json (Ip et le Port)
with open('settings.json') as fichier:
    settings = json.load(fichier)


###############################################
##                 SERVEUR                   ##
###############################################


class ClientThread(threading.Thread): #Définition de notre class, celle-ci correspondra à chaque client

    def __init__(self, ip, port, clientsocket):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))

    def run(self):

        print("/!\ Connexion de %s %s" % (self.ip, self.port, ))

        while True: # Tant que le client est connecté, on récupère les datas qu'il nous envoie puis on lui renvoie une réponse

            dataClient = self.clientsocket.recv(2048) # On récupère la date qui nous a été envoyé
            dataClient = dataClient.decode("utf8") # On décode la data qui a été encodé juste avant son envoi
            print("[", ip, port,"]", dataClient)

            if dataClient == "break":
                print("Client déconnecté...")
                data =  "break"
                data = data.encode("utf8") # On encode la data avant son envoi
                self.clientsocket.sendall(data) # On envoie la data au client correspondant
                break

            # Data que nous allons envoyer au client

            print("Que voulez-vous envoyer au client ", self.ip, self.port, " ?")
            data =  input(">> ")
            data = data.encode("utf8") # On encode la data avant son envoi
            self.clientsocket.sendall(data) # On envoie la data au client correspondant


tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((settings["ip"],settings["port"])) # On définit l'adresse ip et le port de notre serveur

while True: # Cette boucle attends la connexion des clients et les créée selon la class définit plus haut
    tcpsock.listen(10)
    print( "En écoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket) # Création d'un thread réservé au client
    newthread.start()