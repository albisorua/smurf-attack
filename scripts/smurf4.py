from scapy.all import *

ip   = IP(src="192.168.1.109" ,dst="192.168.1.255")
data = "Attack at night"

for i in range(10):
    send(ip/ICMP(seq=i)/data, count=1)