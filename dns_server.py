from scapy.layers.dns import *
from scapy.sendrecv import sniff
import socket

ip = str(socket.gethostbyname(socket.gethostname()))
# filters the requirements needed for this DNS Server
# input: packet
# output: true or false
def filter(packet):
    return (IP in packet
            # filters the following:
            and packet[IP].dst == str(socket.gethostbyname(socket.gethostname()))  # same IP
            and DNS in packet  # contains DNS
            and DNSQR in packet  # contains DNSQR
            and DNSRR not in packet  # contains DNSRR
            and packet[DNS].opcode == 0  # it is a Query type
            and UDP in packet  # supports UDP
            and packet[UDP].dport == 53  # sent to port 53
            and (packet[DNSQR].qtype == 1 or packet[DNSQR].qtype == 12))  # if it is type A(1) or PTR(12)


# checks if the IP sent is in the database
# input: packet
# output: true or false
def exists(packet):
    with open(r"C:\Users\Ben\PycharmProjects\Cyber\dns_server_records\dns_records.txt",
              "r") as file:  # copies file into a variable

        # checks each line if the name exists in it
        for line in file:
            if packet[DNSQR].qname.decode() in line:
                print("Found!!!")
                return True

            else:
                print("NOT FOUND HAHAHAHA")
        return False


# sends the properties in the database by specifying it
# if no type was inputted then print all properties
# input: packet, type of property
# output: the property wanted
def typeof_properties(packet, type=None):
    with open(r"C:\Users\Ben\PycharmProjects\Cyber\dns_server_records\dns_records.txt", "r") as file:

        if type.upper() == 'IP':  # sort of answer
            # iterates through the file and returns the value wanted
            for line in file:
                try:
                    if packet[DNSQR].qname.decode() in line:
                        return line.split(';')[1]
                except:
                    continue

        elif type.upper() == 'NA':

            for line in file:
                try:
                    if packet[DNSQR].qname.decode() in line:
                        return line.split(';')[1]
                except:
                    pass


        return None  # exeptional case (I dont even know if that case is possible)


def send_packet(packet):

    #the following changes are necessary in order to send a valid packet back to the client:
    ans_packet = IP(dst=packet[IP].src,
                    src=str(socket.gethostbyname(socket.gethostname())) /
                        UDP(dport=packet[IP].sport, sport=53) /
                        DNS(id=packet[DNS].id, qr=1, qd=packet[DNSQR], an=
                        DNSRR(rrname=packet[DNSQR].qname.decode(),
                              type=packet[DNSQR].qtype)))

    if packet[DNSQR].qtype == 1:
        ans_packet.show()
        print('-------------------------------------------------')
        ans_packet[DNSRR].rdata = str(typeof_properties(packet, 'ip'))

        ans_packet.show()
        print(str(typeof_properties(packet, 'ip')))
    elif packet[DNSQR].qtype == 12:
        ans_packet = DNS(rdata="Ben-PC DNS Server")

    else:
        pass





def main():
    print(ip)
    print("sniffing...")
    packet = sniff(count=1, lfilter=filter)[0]  # sniffing
    print("sniffing complete.")
    send_packet(packet)


if __name__ == '__main__':
    main()

    # except ValueError and AttributeError and IndexError:
    #     print("The packet does not contain the attribute or value needed")
