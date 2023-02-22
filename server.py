import socket
import threading

class ClientThread(threading.Thread): #Définition de notre class, celle-ci correspondra à chaque client

    def __init__(self, ip, port, clientsocket):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))

    def run(self):

        print("Connexion de %s %s" % (self.ip, self.port, ))

        r = self.clientsocket.recv(2048) # On récupère la date qui nous a été envoyé
        r = r.decode("utf8") # On décode la data qui a été encodé juste avant son envoi
        print(r)

        # Data que nous allons envoyé au client

        print("Que voulez-vous envoyer au client ", self.ip, self.port, " ?")
        data =  input(">> ")
        data = data.encode("utf8") # On encode la data avant son envoi
        self.clientsocket.sendall(data) # On envoie la date au client correspondant

        print("Client déconnecté...")

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("127.0.0.1",12086)) # On définit l'adresse ip et le port de notre serveur

while True: # Cette boucle attends la connextion des clients et les créée selon la class définit plus haut
    tcpsock.listen(10)
    print( "En écoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket) # Création d'un thrad réservé au client
    newthread.start()