###################################################

import socket
import threading

###################################################

host = '0.0.0.0'
port = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

###################################################

def diffuser(message, client_envoyeur=None):
    for ... in ...: # Parcours de tous les client
        if ... # Verification, on envoie que si ce n'est pas le client envoyeur
            client.send(...)

###################################################

def gestion(client):
    ... : # Boucle infinie pour ecouter en permanence
        try:
            message = client.recv(1024)
            diffuser(message, client)
            print(message)
        except:
            index = clients.index(client) # recuperation de l'index du client
            ... # retirer le client de la liste clients
            client.close() # deconnexion du client
            user = pseudos[index]
            diffuser(f'SERVEUR : {user} a quitte le chat'.encode('utf-8'))
            ... # retirer le pseudo du client de la liste pseudos
            break
    
###################################################

def connexions():
    ... : # Boucle infinie pour ecouter en permanence
        client, address = server.accept() # recuperation des informations du client
        print(f'SERVEUR : Connexion etablie avec {str(address)}')
        pseudo = client.recv(1024).decode('utf-8') # La premiere chose qu'enverra le client est son pseudo, nous pouvons donc traite ce premier messsage
        ... # ajouter le client et son pseudo aux liste clients et pseudos
        ...

        print(f'SERVEUR : Nouvel utilisateur {pseudo} connecte')
        diffuser(f'SERVEUR : {pseudo} a rejoint le chat'.encode('utf-8'))

###################################################

thread = threading.Thread(target=gestion, args=(client,))
# Creation d'un thread ayant pour cible notre fonction gestion
thread.start()
# Lancement du thread

###################################################

connexions()

###################################################

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.1.54', 5555)) # modifier l'adresse ip

###################################################

client.send(pseudo.encode('utf-8'))

###################################################

def envoyer(message):
    client.send(message.encode('utf-8'))

###################################################

def ecrire():
    ... # faire tourner la demande a l'infinie
        message = ... # demander a l'utilisateur son message
        ... # envoyer le message
    
###################################################

def recevoir():
    while True:
        message = client.recv(1024).decode('utf-8')
        if 'SERVEUR' in message:
            print("\n")
            print("Message du serveur :\n")
            print(message)
            print("\n")
        else:
            print(message)

###################################################

receive_thread = threading.Thread(target=...)
receive_thread.start()

write_thread = threading.Thread(target=...)
write_thread.start()

###################################################

from chiffre import *