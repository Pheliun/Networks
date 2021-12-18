import socket

my_socket = socket.socket()
my_socket.connect(("127.0.0.1", 8800))

inpt = 'lolnubwtfudonthavedowhilelooplolgetlmaoed'
while inpt != 'EXIT':
    inpt = input('please enter input')
    leng = str(len(inpt)).zfill(2)
    my_socket.send((leng + inpt).encode())

    leng = int(my_socket.recv(2).decode())
    print(my_socket.recv(leng).decode())

    continue
my_socket.close()
