import socket
import threading

###################################################

host = '0.0.0.0'
port = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
pseudos = []

def diffuser(message, client_envoyeur=None):
    for client in clients: # Parcours de tous les client
        if client_envoyeur != client: # Verification, on envoie que si ce n'est pas le client envoyeur
            client.send(message)


def gestion(client):
    while True : # Boucle infinie pour ecouter en permanence
        try:
            message = client.recv(1024)
            diffuser(message, client)
            print(message)
        except:
            index = clients.index(client) # recuperation de l'index du client
            clients.pop(index) # retirer le client de la liste clients
            client.close() # deconnexion du client
            user = pseudos.pop(index)
            diffuser(f'SERVEUR : {user} a quitte le chat'.encode('utf-8'))
            break


def connexions():
    while True : # Boucle infinie pour ecouter en permanence
        client, address = server.accept() # recuperation des informations du client
        print(f'SERVEUR : Connexion etablie avec {str(address)}')
        pseudo = client.recv(1024).decode('utf-8') # La premiere chose qu'enverra le client est son pseudo, nous pouvons donc traite ce premier messsage
        clients.append(client) # ajouter le client et son pseudo aux liste clients et pseudos
        pseudos.append(pseudo)

        print(f'SERVEUR : Nouvel utilisateur {pseudo} connecte')
        diffuser(f'SERVEUR : {pseudo} a rejoint le chat'.encode('utf-8'))

        thread = threading.Thread(target=gestion, args=(client,))
        # Creation d'un thread ayant pour cible notre fonction gestion
        thread.start()
        # Lancement du thread

connexions()
