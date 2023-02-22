import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 12086)) # Connexion au serveur


while True:
    print("Message à envoyer au serveur:")
    data = input(">> ")
    data = data.encode("utf8") # On encode le message
    s.sendall(data) # On envoie le message au serveur sous sa version codé

    # Le Serveur renvoit quelque chose

    data2 =''
    data2 = s.recv(1024)
    data2 = data2.decode("utf8") #On le decode car encodé coté serveur avant l'envoi
    if data2 == "break":
        break
    print(data2) # On affiche le contenu de ce que nous avons reçu