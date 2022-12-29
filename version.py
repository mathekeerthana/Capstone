'''import sys
# sys is a package
# numpy #pyodbc :: pip install <package name>


print("current version:",sys.version)'''
'''
import socket
print(socket.gethostname())'''

import socket
hostname = socket.gethostname()
print(hostname)


hostname1 = socket.gethostbyname(hostname)
print(hostname1)
