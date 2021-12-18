from scapy.layers.dns import *
from scapy.sendrecv import sniff
import os
os.sys.path.append('/usr/local/lib/python2.7/site-packages')
os.sys.path.append('/usr/bin')

def filter_dns(packet):
    return (DNS in packet and packet[DNS].opcode == 0) #filters query dns packets

print("sniffing...")
packets = sniff(count=10,lfilter=filter_dns) #sniffing
print("sniffing complete.")

for packet in packets:
    packet.show()

    # if not TCP in packet or UDP in packet and packet[TCP].dport == 53 or packet[UDP].dport ==53: #port 53
    #     print("Packet does not meet the requirements")
    #     break

    # if not packet[DNSQR].qtype == 1 and packet[DNSQR].qtype == 12: #type PTR or A
    #     print("Packet does not contain the requirements")
    #     break

    file = open(r"C:\Users\Ben\PycharmProjects\Cyber\dns_server_records\dns_records.txt", "r")
    if packet[DNS].qname == file.read().split(' ')[0]:
        print(file.read())

