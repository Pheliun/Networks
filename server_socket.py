import socket
import datetime
import random
import glob
import os
import shutil
import subprocess
#import pyautogui

server_socket = socket.socket()
server_socket.bind(("0.0.0.0", 8800))
server_socket.listen()
print("Server is up and running")

(client_socket, client_address) = server_socket.accept()
print("Client connected")
data = 'lolnubwtfudonthavedowhilelooplolgetlmaoed'
while data != 'EXIT':

    try:
        leng = int(client_socket.recv(2).decode())
    except ValueError:
        reply = "It appears that your input is invalid..."
        leng = str(len(reply)).zfill(2)
        client_socket.send((leng + reply).encode())
        continue

    data = client_socket.recv(leng).decode()
    print(data)
    if (data == 'TIME'):
        reply = 'The time now is: ' + str(datetime.datetime.now())

    elif (data == 'WHORU'):
        reply = 'I Am J.A.R.V.I.S'

    elif (data == 'RAND'):
        reply = str(random.randint(1, 10))

    elif (data.startswith('DIR')):  # NOT WORKING FOR SOME REASON AAAAAAAAAAAAAAAAAAAAAAAA
        reply = str(glob.glob(data[4:]))
    elif (data.startswith('DELETE')):
        os.remove(data[7:])
        reply = 'Successfully deleted!'
    elif (data.startswith('COPY')):
        copy = (data[5:].split(' '))
        print(copy[0] + " " + copy[1])
        shutil.copy(copy[0], copy[1])
        reply = 'Successfully copied!'
    elif (data.startswith('EXECUTE')):  # NOT WORKING FOR SOME REASON AAAAAAAAAAAAAAAAAAAAAAAA
        print(data[8:])
        subprocess.call(data[8:])
        reply = 'Successfuly executed!'

    else:
        reply = 'invalid input'
        leng = str(len(reply)).zfill(2)
        client_socket.send((leng + reply).encode())
        continue

    print(reply)
    leng = str(len(reply)).zfill(2)
    client_socket.send((leng + reply).encode())
    continue
client_socket.close()
server_socket.close()
