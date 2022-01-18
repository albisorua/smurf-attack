from scapy.all import *

ip   = IPv6(src="fe80::a00:27ff:fecc:898c", dst="ff02::1")
data = "Attack at night"

for i in range(10):
    send(ip / ICMPv6EchoRequest(seq=i, data=data), count=1)