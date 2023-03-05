# Client / Serveur - Python3

/!\ Ce projet peut être soumis à évolution

## Qu'est-ce que c'est ?

Cette template vous donne accès à deux scripts "client.py" & "server.py". Avec ces deux scripts vous pouvez de façon très simple et automatiser créer une communication serveur/client
(A noté que cette template demande à ce que python3 soit installé sur la machine)

## Utilisation

### Cloner la repository sur votre Machine en Local.

```bash
git clone https://github.com/MrPaulon/Client-Server-Python3/
cd Client-Server-Python3
```

### Configuration

Pour configurer rien de plus simple, il suffit d'exécuter le script "configuration.py" et de suivre les instructions, tel que:
```bash
python3 configuration.py
```

### Utiliser

Pour créer notre première communication il faut dans un premier temps allumer le serveur, car c'est lui qui va attendre la connexion des clients et répondre à leurs demandent, pour ce faire il suffit de faire :
```bash
python3 server.py
````
 Si le serveur est correcteur démmaré il drevrait vous affichez "En écoute..."
 Si c'est le cas il ne vous reste plus cas démmarer votre premier client. Pour ce faire ouvrer un nouveau terminal, rendez vous dans notre dossier et effectuez la commande suivante:
 ```bash
 python3 client.py
 ```
 
 Bien joué vous avez mis en place une communication entre un serveur et un client ! :)
