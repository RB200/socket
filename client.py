from ipaddress import ip_address
import socket
from threading import Thread

name = input('Please enter your name: ')
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip = '127.0.0.1'
port = 8000

client.connect((ip,port))
print('Connected to server')

def receive():
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message == 'NICKNAME':
                client.send(name.encode('utf-8'))
            else:
                print(message)
        except:
            print('An error occured')
            client.close()
            break

def write():
    while True:
        message = '{}: {}'.format(name,input(''))
        client.send(message.encode('utf-8'))
        
receive_thread = Thread(target=receive)
receive_thread.start()

write_thread = Thread(target=write)
write_thread.start()