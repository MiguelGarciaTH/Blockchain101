#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a rock scissors paper game python's implementation

"""
import argparse
import socket
import threading
import time
import fcntl, os
import random
import hashlib
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from rsa_signatures import RSASignature

def bytes_to_int(bytes):
    result = 0
    for b in bytes:
        result = result * 256 + int(b)
    return result

def send(sock, data):
    size = len(data)
    sock.sendall(size.to_bytes(4, byteorder = 'big'))
    #print("\nSENDING " +b64encode(data).decode('utf-8'))
    sock.sendall(data)

def receive(client_socket):
    rcv_len = bytes_to_int(client_socket.recv(4))
    data = client_socket.recv(rcv_len)
    #print("\nRECEIVING  " +b64encode(data).decode('utf-8'))
    return data

def am_i_winner(option1, option2):
    if option1.lower() == "rock" and option2.lower()  == "paper":
        return False
    if option2.lower() == "rock" and option1.lower()  == "paper":
        return True
    if option1.lower() == "paper" and option2.lower()  == "scissors":
        return False
    if option2.lower() == "paper" and option1.lower()  == "scissors":
        return True
    if option1.lower() == "rock" and option2.lower()  == "scissors":
        return True
    if option2.lower() == "rock" and option1.lower()  == "scissors":
        return False
    else:
        return "Draw"

def rps_encrypt(key, data):
    e_cipher = AES.new(key, AES.MODE_ECB)
    return e_cipher.encrypt(pad(data,AES.block_size))

def rps_decrytp(key, data):
    d_cipher = AES.new(key, AES.MODE_ECB)
    return unpad(d_cipher.decrypt(data),AES.block_size)

def play(socket):
    key = b'Sixteen byte key'
    while True:
        print("Select an option: Rock, Scissors or Paper")
        option = input()
        print("Me: %s" %(option))

        rand = random.randrange(100)
        hashed = hashlib.sha256(bytes(str(rand)+option, 'utf-8'))

        bytes_to_send = hashed.hexdigest().encode('utf-8')
        encrypted_bytes = rps_encrypt(key, bytes_to_send)

        signature = RSASignature.sign(encrypted_bytes)#bytearray(os.urandom(1000000))

        send(socket, signature)
        send(socket, encrypted_bytes)

        rcv_signature = receive(socket)
        data = receive(socket)

        if not RSASignature.verify(data,rcv_signature):
            break

        encrypted_bytes2 = rps_decrytp(key, data)
        hash_rcv =  encrypted_bytes2.decode('utf-8')

        encrypted_bytes = rps_encrypt(key, (str(rand)+":"+option).encode('utf-8'))
        send(socket, encrypted_bytes)
        data2 = receive(socket)

        encrypted_bytes2 = rps_decrytp(key, data2)
        decrypted_data2 =  encrypted_bytes2.decode('utf-8').split(":")

        hashed2 = hashlib.sha256(bytes(str(decrypted_data2[0])+decrypted_data2[1], 'utf-8'))

        if hashed2.hexdigest() == hash_rcv:
            if data:
                print("Openent: %s" % decrypted_data2[1])
            print("Did I win? %s" % am_i_winner(option, decrypted_data2[1]) )

    socket.close()

def lobby_thread(server, host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.connect((host, port))
        t2 = threading.Thread(target=play, args=(sock,))
        t2.start()
        t2.join()
    except ConnectionRefusedError:
        print("Waiting for the other player")
        while True:
            server.listen(1)
            clientsock, clientAddress = server.accept()
            t2 = threading.Thread(target=play, args=(clientsock, ))
            t2.start()
            t2.join()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((socket.gethostname(), MYPORT))
    server.listen()
    print("Server sockect is ready on port %d" % MYPORT)
    t1 = threading.Thread(target=lobby_thread, args=(server, HOST, PORT))
    t1.start()
    t1.join()

# PARSING CMD PARAMETERS
ConnectionInfo = argparse.ArgumentParser()
ConnectionInfo.add_argument("-ip",  default=socket.gethostname())
ConnectionInfo.add_argument("-sp", type=int, default='5556')
ConnectionInfo.add_argument("-mp", type=int, default='5557')

ConnectionInfoParsed = ConnectionInfo.parse_args()
# Saves the parsed IP and Port
HOST = ConnectionInfoParsed.ip
PORT = ConnectionInfoParsed.sp
MYPORT = ConnectionInfoParsed.mp

if __name__ == "__main__":
    main()
