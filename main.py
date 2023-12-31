import threading
import socket
import hashlib

import rsa

import time

public_key, private_key = rsa.newkeys(1024)
public_partner = None



choice = input("Do you want to host (1) or to connect (2): ")

if choice == "1":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("host: " + socket.gethostname())
    print("port: 1234")
    server.bind((socket.gethostname(), 1234))
    server.listen()

    client, _ = server.accept()
    client.send(public_key.save_pkcs1("PEM"))
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))

elif choice == "2":
    hostname = input("Enter the hostname: ")
    port = int(input("Enter the port number: "))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((hostname, port))

    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
    client.send(public_key.save_pkcs1("PEM"))
else:
    print("Invalid choice")
    exit()

def sending_message(c):

    while True:
        files = []
        hashes = []
        while len(hashes) < 5:
            msg = input("")
            try:
                with open(msg, "rb") as f:
                    digest = hashlib.file_digest(f, "sha256")
                    files.append(msg)
                    hashes.append(digest.hexdigest())
            except Exception as e:
                print("File does not exist!")
                continue
        for h in hashes:
            c.send(rsa.encrypt(h.encode(), public_partner))
            print("You: " + h)
            time.sleep(0.5)
        break

def receiving_message(c):
    count = 0
    while True:
        msg = rsa.decrypt(c.recv(1024), private_key).decode()
        print("Stranger: " + msg)
        count += 1
        if count == 5:
            break

threading.Thread(target=sending_message, args=(client, )).start()
threading.Thread(target=receiving_message, args=(client, )).start()