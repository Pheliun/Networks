from scapy.layers.dns import *
from scapy.sendrecv import *
import socket

syn_packet=IP(dst='www.google.com')/TCP(dport=80,seq=123,flags='S')
send(syn_packet)
syn_ack_packet = sr1(syn_packet)
syn_ack_packet.show()
ack_packet = IP(dst='www.google.com')/TCP(dport=80,seq=syn_ack_packet[TCP].ack,ack=syn_ack_packet[TCP].seq+1,flags='A')
send(ack_packet)
