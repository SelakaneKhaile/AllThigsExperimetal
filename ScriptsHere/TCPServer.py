"""
By Slekane Khaile
Discription: This is a simple TCPServer in python
"""
from http import client
from logging.config import listen
from pydoc import cli
import socket
import threading
from traceback import print_tb
from urllib import request

IP = '0.0.0.0'
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET, socket
    .SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        client, address = server.accept()
        print(f'[*] Accepted connection from: {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Recived: {request.decode("utf-8")}')
        sock.send(b'OK!')

if __name__=='__main__':
    main()