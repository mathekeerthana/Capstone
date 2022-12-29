import os , ipaddress
os.system('cls') #os.system will clear the console at the start of the exxecution
while True:
    ip = input("Enter IP Address:")
    try:
        print(ipaddress.ip_address(ip))
        print("Ip valid")
    except:
        print('-' *50)
        print('IP is not valid')
    finally:
        if ip=='pineapple':
            print("Script Finished")
            break

#<package : ipaddress>.<ip_address>.<attribute :ip>