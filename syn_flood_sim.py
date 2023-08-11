from scapy.all import *

target_ip = "127.0.0.1"
target_port = 1729

ip = IP(dst=target_ip)
tcp = TCP(sport=RandShort(), dport=target_port, flags="S")

raw = Raw(b"X"*1024)

p = ip / tcp / raw

cnt = int(input("Enter number of packets: "))
send(p, count=cnt, verbose=0)

print("Packets sent!")
