#Abdallah Nofal's Ping Tool
#100162893
#Final Project

from icmplib import ping # PLEASE INSTALL ICMPLIB FIRST https://pypi.org/project/icmplib/
import re
from datetime import datetime

def isValidWebsiteFormat(addressInput):
    websiteFormat = re.compile(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$') # Ensures input is in website format
    return bool(re.match(websiteFormat, addressInput))

addresses = []
successfulPing = failedPing = 0

address = input("Enter IP addresses of websites, networks or domains to check their ping. Type '0' when done: ")

try:
    while address != '0':
        if isValidWebsiteFormat(address):
            addresses.append(address)
            print(f"{address} successfully added!")
        else:
            print(f"{address} is not in a valid website format. Please enter a valid address.")
    
        address = input("Enter another IP address or type '0' when done: ")
    
    if len(addresses) > 0:
        while True:
            try:
                timeout = float(input("Enter timeout for ping requests (in seconds, between 0 and 10): "))
                if 0 <= timeout <= 10:
                    break
                else:
                    print("Timeout must be between 0 and 10 seconds. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
            
        print("Thank you! Calculating results for the following addresses:")
        
        for i, item in enumerate(addresses, 1):
            print(f"{i}. {item}")
            
        for address in addresses:
            result = ping(address, count = 4, interval = 1, timeout = timeout)
            
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"\n{timestamp} - {address} ({result.address}): {'Successful Connection' if result.is_alive else 'Failed Connection'}")
        
            if result.is_alive:
                print(f" - Packets Sent: {result.packets_sent}")
                # The number of requests transmitted to the remote host
                print(f" - Packets Received: {result.packets_received}")
                # The number of ICMP responses received from the remote host
                print(f" - Average Round Trip Time: {result.avg_rtt}ms")
                # The average round-trip time in milliseconds
                print(f" - Minimum Round Trip Time: {result.min_rtt}ms")
                # The minimum round-trip time in milliseconds
                print(f" - Maximum Round Trip Time: {result.max_rtt}ms")
                # The maximum round-trip time in milliseconds
                print(f" - Jitter: {result.jitter}ms")
                # The jitter in milliseconds, defined as the variance of the latency
                # of packets flowing through the network
                successfulPing += 1
            else:
                print(f" - Packet loss: {result.packet_loss}%")
                # Packet loss occurs when packets fail to reach their destination
                failedPing += 1
        
        print("\nSummary:")
        print(f"- Addresses Provided: {failedPing + successfulPing}")
        print(f"- Successful connections: {successfulPing}")
        print(f"- Failed connections: {failedPing}")
    else:
        print("No Address Given!")

except Exception as e:
    print(f"An error occurred: {e}")