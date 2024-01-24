import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("195.37.16.58", 1234))

s.listen(5)

while True:

    clientsocket, address = s.accept()

    print("Connection from {address} has been established")

    clientsocket.send(bytes("You did it!", "utf-8"))


