import socket
import datetime

today = str(datetime.datetime.today())
print(today)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET - address family specifying what addresses in socket can communicate with
# used for communicating over the internet
# AF_BLUETOOTH - used for comm over Bluetooth
# socket.SOCK_STREAM - use TCP to ensure delivery (fact check)

s.bind(("", 8888))
# bind socket to TCP port 8888

s.listen(10)
print("server up and listening")
# set length of queue (process multiple requests at the same)

while True:
    connect, address = s.accept()
    print("connection made")
    resp = (connect.recv(1024)).strip()  # limit requests to 1024 bytes
    print(resp)
    message = input("> ")
    connect.send(message.encode())
    connect.close()  # close the connection when finished