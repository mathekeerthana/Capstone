import socket
import subprocess
import sys
from datetime import datetime
#subprocess.call('clear',shell=True)

#Ask for input
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)
print(" "*50)
print("please wait, scanning remote host", remoteServerIP)
print(" "*50)

#Check the data and time the scan was started
t1=datetime.now()
# using the range function to specify ports
#Also we do error handling
try:
    for port in range(1,5000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP,port))
        if result == 0:
            print("port {}:      Open".format(port))
            sock.close()
except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit()
except socket.error:
    print("Couldn't connect to server")
    sys.exit()