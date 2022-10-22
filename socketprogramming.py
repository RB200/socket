from threading import Thread
import socket 

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

server.bind((ip_address,port))

server.listen()

clients = []
names = []

print('Server is running')

def clientthread(con,name):
    con.send('Welcome to this chatroom!'.encode('utf-8'))
    while True:
        try:
            message = con.recv(2048).decode('utf-8')
            if message: 
                print(message)
                broadcast(message,con)
            else:
                remove(con)
                remove_nickname(name)
        except: 
            continue

def broadcast(msg,con):
    for cli in clients:
        if cli != con:
            try:
                cli.send(msg.encode('utf-8'))
            except:
                remove(cli)

def remove(con):
    if con in clients:
        clients.remove(con)

def remove_nickname(name):
    if name in names:
        names.remove(name)
        

while True:
    con,add = server.accept()
    con.send('NICKNAME'.encode('utf-8'))
    name = con.recv(2048).decode('utf-8')
    clients.append(con)
    names.append(name)
    message = '{} joined!'.format(name)
    print(message)
    broadcast(message,con)
    #print(add[0] + 'connected')
    newthread = Thread(target=clientthread,args=(con,name))
    newthread.start()


