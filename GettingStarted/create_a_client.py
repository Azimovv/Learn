import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
# set port
port = 8888

s.connect((host, port))

msg = s.recv(5)
s.close()

print("{}".format(msg))