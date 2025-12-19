import socket
import re


# Regular expression Pattern, this will be used to recognize IPV4 address.
ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
# Regular Expression Pattern for the range of Port to scan
# Based on the lowest range and highest range
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

# Specifying the upper and lower bounds for the port range
min_port = 0
max_port = 65536

print("--------------------------------------------------------------------------")
print("&&&& - PORT SCANNER V1.1 - &&&& \n\n")
print("--------------------------------------------------------------------------")

open_ports = [] # An array to store all the ports that will be found open

while True:
    # IP input and validation
    ip_add_input = input("\nPlease enter the ip address that you want to scan: ")
    if ip_add_pattern.search(ip_add_input):
        print(f"{ip_add_input} is a valid ip address")
        break

while True:
    # Now we implement main code here
    print("Please enter the Port Range to scan (Min Range - Max Range)")
    port_range = input("\nEnter the port range: ")
    # From what I see, this replaces the empty space in between them
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        # Extracting the minimum (first part before hypen) and the maximum (second part after hypen)
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

print(port_max)
print(port_min)

# Scanning through the range using a loop

for port in range(port_min, port_max + 1):
    #connect to the targetted machine:
    try:
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            s.settimeout(0.2)

            s.connect((ip_add_input, port))
            print(f"Currnet Port number: {port}")
            # This line will run if socket was sucessful in forming a connection with the domain
            open_ports.append(port)

    except:
        pass


for port_info in open_ports:
    # Now we print if we find any open ports:
    print(f"Port {port_info} is open on {ip_add_input}.")