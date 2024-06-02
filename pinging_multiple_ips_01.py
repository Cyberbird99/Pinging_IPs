# I'll make a code pinging the whole subnetworking
# I'll write the fixed first three octets.
# And loop the last octet from 0 to 254.

import platform
import os

# Define the prefix to begin pinging
ip_prefix = "192.168.0."
# Determine the current OS
current_os = platform.system().lower()
# Loop from 0 to 254
for final_octet in range(254):
    # Assign IP to ping to a variable
    # Adding 1 to final_octet because loop starts at 0
    ip = ip_prefix + (str(final_octet + 1))
    if current_os == 'windows':
        # Build the ping command for windows
        ping_cmd = f"ping -n 1 -w 2 {ip} >null"
    else:
        # Build the ping command for the other OSs
        ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"

    # Execute command and capture eit code
    exit_code = os.system(ping_cmd)
    # print results to console
    if exit_code == 0:
        
        print("{0} is online".format(ip))
    else:
        print("{0} is NOT online".format(ip))

    # else part of the condition could preferably be omitted.
    # so only online Ips appear on console.

