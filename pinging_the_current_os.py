# Code will determine the current OS first and start scanning
# whether it's windows or Linux 

import os
import platform

# Assign Ip to ping to a variable
ip = "127.0.0.1"
# Determine the current OS
current_os = platform.system().lower()
if current_os == "windows":
    # Build the ping commmand for windows
    ping_cmd = f"ping -n 1 -w 2 {ip} > null"
    # for number of attempts for windows, use -n NOT -c
else:
    # Build the ping command for any different OS
    # As other operating systems are Unix-based, we utilize the same ping command.
    ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"
    
    # Execute the command and capture the exit code. 
    # It will yield a number: 0 denotes success, 
    # while any other number signifies failure.
    exit_code = os.system(ping_cmd)

