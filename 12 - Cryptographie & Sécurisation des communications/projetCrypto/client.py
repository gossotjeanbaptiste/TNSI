import socket
import threading

pseudo = input("Pseudo ? : ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))

# première connexion, on envoie le pseudo
client.send(pseudo.encode('utf-8'))

def envoyer(message):
    client.send(message.encode('utf-8'))

def ecrire():
    while True:
        message = input("")
        envoyer(message)

def recevoir():
    while True:
        message = client.recv(1024).decode('utf-8')
        if 'SERVEUR' in message:
            print("\n")
            print(message)
            print("\n")
        else:
            print(message, 13)


receive_thread = threading.Thread(target=recevoir)
receive_thread.start()

write_thread = threading.Thread(target=ecrire)
write_thread.start()
