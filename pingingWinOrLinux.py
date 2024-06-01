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
    # Build the ping command for any other OS
    ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"
    # Execute the command and capture exit code.
    # It will give out a number, 0 for success, 
    # other number for failure
    exit_code = os.system(ping_cmd)

