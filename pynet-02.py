import socket
s=socket.socket()
print("Socket successfully created")
port =40674
s.bind(('',port))
print("Socket binded to %s" %(port))
s.listen(5)
print("socket is listening")
while True:
    # Establish connection with client
    c,addr =s.accept()  # single line, multivariable assignment

    #print() || debugger
    print(c)
    print('Got connection from',addr)
    c.send(b'Thank you for connecting')     # b--> transering bytes from one machine to another machine
    c.close()