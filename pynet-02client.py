import socket
s=socket.socket()
port = 40674    # Define the port on ehich you want interrupt it
s.connect(('127.0.0.1',port))   # connect to the server on local computer
print(s.recv(1024))      # receive data from the server
s.close()   # close the connection

