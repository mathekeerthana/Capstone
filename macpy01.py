#CODE REFACTORING

#pip install getmac
from getmac import get_mac_address as gma
print(gma())

#pip install uuid
import uuid

#printing the values of unique MAC
#address using uuid and getnode() function
print(hex(uuid.getnode()))

import uuid
print("The MAC address in formatted way is :",end="")
print(':'.join(['{:02x}'.format((uuid.getnode()>>ele) & 0xff)
for ele in range(0,8*6,8)][::-1])) #-1 -ve indexing