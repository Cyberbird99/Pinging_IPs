#!/usr/bin/env python3
# Example of pinging one single Ip

import platform
import os

# Assign Ip to ping to a variable
ip = "127.0.0.1"
# I used the loopback Ip address, which should work on all devices
# and networks.

# Build ping command
ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"
#I limited the number of attempts to send to the target 
# with -c and specified how long to wait for a response with -w
# to remove the currenty unnecessary information I redirected it to 
# /dev/null, which is a special location in Linux as a garbage bin.

# Execute command and capture exit code
exit_code = os.system(ping_cmd)
# It'll give out a number.
# It's a success/failure status. 0 means success, 
# any other number failure

# Print the results to console
print(exit_code)