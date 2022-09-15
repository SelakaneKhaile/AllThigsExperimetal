"""
By Slekane Khaile
Discription: This is a simple TCP client in python
"""
import socket
from urllib import response

target_host = "127.0.0.1"
tagrget_pot = 9998

#making a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#then connect to the client 
client.connect((target_host, tagrget_pot))

#send some data 
client.send(b"Hello ind3x did this shit!\r\n")

#recieve some data
response = client.recv(4096)

print(response.decode())

client.close()