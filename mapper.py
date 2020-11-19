import sys
import socket
from colorama import Fore, Back, Style
from datetime import datetime
# Define our target
print(Fore.RED)
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # Translate Hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 mapper.py <ip> or <site>")
#Add a banner
print(Fore.YELLOW)
print("-" * 50)
print(Fore.CYAN)
print("Made BY @PurpleHattt - Github")
print(Fore.RED)
print("Time started: "+str(datetime.now()))
print("\nScanning target: "+target)
print(Fore.YELLOW)
print("-" * 50)
print(Fore.RESET)
try:
    port1 = int(input("Write down starting port. Example - \"22\":\n"))
    port2 = int(input("Write down ending of ports. Example - \"445\":\n"))
    for port in range (port1,port2):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) # returns an error indicator
        if result == 0:
            print("Port {} is open".format(port))
        else:
            print("Port {} is not open".format(port))
        s.close

except KeyboardInterrupt:
    print(Fore.RED)
    print("\nExitting.")
    sys.exit
except socket.gaierror:
    print("Hostname could hot be resolved.")
except socket.error:
    print("Could not connect to server.")
    sys.exit