import socket
import threading

pseudo = input("Pseudo ? : ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("172.19.0.169", 5555))  # modifier l'adresse ip

client.send(pseudo.encode("utf-8"))


def envoyer(message):
    client.send(message.encode("utf-8"))


def ecrire():
    while True:  # faire tourner la demande a l'infinie
        message = input("message: ")  # demander a l'utilisateur son message
        envoyer(message)  # envoyer le message


def recevoir():
    while True:
        message = client.recv(1024).decode("utf-8")
        if "SERVEUR" in message:
            print("\n")
            print("Message du serveur :\n")
            print(message)
            print("\n")
        else:
            print(message)


receive_thread = threading.Thread(target=recevoir)
receive_thread.start()

write_thread = threading.Thread(target=ecrire)
write_thread.start()
