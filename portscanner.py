import socket
import ipaddress
import sys 

ip= input("Enter ip_address : ")
try:
    ipaddress.IPv4Address(ip)

except ipaddress.AddressValueError:
    print("invalid ip address")
    sys.exit()
    
port = input("enter the port number ").split()

for numbers in port:

    try:
        number = int(numbers)
        if number < 1 or number > 65535:
            print("enter valid port number")
            continue
    except ValueError:
        print(f"please enter a vlaid port number")
        continue

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(2)

    try:
        result = s.connect_ex((ip, number))
        if result ==0:
            print(f"port {number} is open")
        else:
            print(f"Port {number}: connection failed, error code {result}")
    except socket.timeout:
        print (f"Port {number}: connection timed out")
    finally:
        s.close()
