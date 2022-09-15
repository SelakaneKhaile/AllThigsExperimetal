"""
By Slekane Khaile
Discription: This is a simple UDP client in python
"""
import socket

target_host = "127.0.0.1"
tagrget_pot = 9997

#making a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send some data 
client.sendto(b"Vualaa!",(target_host, tagrget_pot))

#recieve some data
data, addr = client.recvfrom(4444)

print(data.decode())

client.close()