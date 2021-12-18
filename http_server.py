import os
import socket

server_socket = socket.socket()
server_socket.bind(('0.0.0.0',80))
while True:
    server_socket.listen(0)
    (client_socket,client_adress) = server_socket.accept()
    request = client_socket.recv(1024).decode()
    #request = 'GET C:\Users\Ben\Downloads\webroot\index.html HTTP/1.1\r\n'
    print(request)
    if not (request.startswith('GET ') and ' HTTP' in request and request.endswith(r'\r\n') ):
        print('Invalid link or input')
        client_socket.close()
        continue

    spl = request.split(' ')
    print(len(spl))
    #split the code-line below (list index out of range
    client_socket.send((spl[1].split('\\')[len(spl)]).encode())
    if not os.path.isfile(spl[1]):
        print('This file does not exist')
        client_socket.close()
        continue

    reply = open(spl[1],'rb')

    client_socket.send((reply))
    reply.close()

server_socket.close()