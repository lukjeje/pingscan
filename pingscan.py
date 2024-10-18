import re
import ipaddress
import subprocess


a = """
██████╗ ██╗███╗   ██╗ ██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗██║████╗  ██║██╔════╝ ██╔════╝██╔════╝██╔══██╗████╗  ██║
██████╔╝██║██╔██╗ ██║██║  ███╗███████╗██║     ███████║██╔██╗ ██║
██╔═══╝ ██║██║╚██╗██║██║   ██║╚════██║██║     ██╔══██║██║╚██╗██║
██║     ██║██║ ╚████║╚██████╔╝███████║╚██████╗██║  ██║██║ ╚████║
╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
"""

print(a)

print("---------------------------------------------------")
print("")

def get_ip_range():
    while True:
        ip_input = input("Enter an IP address range (e.g., 192.168.5.0/24): ")
        ip_input = ip_input.strip()

        try:
            # Validate the CIDR notation
            network = ipaddress.ip_network(ip_input, strict=False)  # strict=False allows for single IPs too
            start_ip = str(network[0])
            end_ip = str(network[-1])
            print(f"Valid IP range entered: {start_ip} - {end_ip}")
            print("++++++++++++++++++++++++++")

            # Exclude the broadcast address (last IP)
            ip_list = [str(ip) for ip in network if ip != network.broadcast_address]
            print("++++++++++++++++++++++++++")
            break
        except ValueError:
            print("Invalid IP range. Please enter a valid CIDR notation (e.g., 192.168.5.0/24).")
    
    return start_ip, end_ip, ip_list








q = input("Type 'P' for normal ping OR Type 'A' for arp ping: ")









if q == "A":

 def arping_ip_range(ip_list):
    """
    ARP pings all IP addresses in the provided list.
    """
    active_ips = []

    for ip in ip_list:
        command = ["arping", "-c", "1", ip]  # Send 1 ARP request
        response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if response.returncode == 0:
            print(f"{ip} is active")
            active_ips.append(ip)
        else:
            print(f"{ip} is not reachable")
    
    return active_ips

 # Call the function to get the IP range
 start_ip, end_ip, ip_list = get_ip_range()

 # Now ARP ping all the addresses in the list
 print("ARP Pinging network...")
 active_ips = arping_ip_range(ip_list)
 print(f"\nActive IPs: {active_ips}")








if q == "P":
 def ping_ip_range(ip_list):
    """
    Pings all IP addresses in the provided list using standard ICMP ping.
    """
    active_ips = []

    for ip in ip_list:
        # Ping command: -c 1 for 1 ping, -W 1 for 1-second timeout (may vary by system)
        command = ["ping", "-c", "1", "-W", "1", ip]  
        response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if response.returncode == 0:
            print(f"{ip} is active")
            active_ips.append(ip)
        else:
            print(f"{ip} is not reachable")
    
    return active_ips

# Call the function to get the IP range
start_ip, end_ip, ip_list = get_ip_range()

# Now ping all the addresses in the list
print("Pinging network...")
active_ips = ping_ip_range(ip_list)
print(f"\nActive IPs: {active_ips}")    
