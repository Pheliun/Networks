from scapy.sendrecv import *
from scapy.layers.dns import *

port_num = 39;
while port_num <= 1024:
    port_num+=1
    syn_packet= IP(dst='www.google.com')/TCP(dport=port_num,seq=123,flags='S')
    send(syn_packet)
    syn_ack_packet = sr1(syn_packet, timeout=2)
    # ack_packet = IP(dst='www.google.com')/TCP(dport=port_num,seq=syn_ack_packet[TCP].ack,ack=syn_ack_packet[TCP].seq+1,flags='A')
    # send(ack_packet)
    if syn_ack_packet != null or syn_ack_packet[TCP].rst != 1:
        print("port "+port_num+"is active\n")

print("loladiasenseisucks")