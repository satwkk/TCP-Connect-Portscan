import threading
import optparse
import socket
import sys
import os 

def connScan(target_host, target_port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.connect((target_host, target_port))
        print(f"{target_port} open")
        s.send(b"EHLO\r\n")
        response = s.recv(1024)
        if res:
            print(str(response))
        else:
            pass
        s.close()
    except:
        print(f"{target_port} not open on {target_host}")

def portScan(hostname, ports):
    target_ip = socket.gethostbyname(hostname)
    try:
        print(f"{target_ip} is the ip for {hostname}")
    except:
        print(f"Couldn't find any IP for {hostname}")
    try:
        target_name = socket.gethostbyaddr(target_ip)
        print(f"Scan results for {target_name[0]}")
    except:
        print(f"Scan results for {target_ip}")
    for port in ports:
        print(f"Scanning port {port}")
        connScan(hostname, int(port))

if __name__ == "__main__":
    parser = optparse.OptionParser("[*] Usage: %prog -H '<target host>' '<target port>'")
    parser.add_option("-H", type="string", help="Specify Target Hostname", dest="target_host")
    parser.add_option("-P", type="string", help="Specify Target Port", dest="target_port")
    (options, args) = parser.parse_args()
    #tHost = options.target_host
    #tPort = str(options.target_port)
    tHost = "192.168.56.1"
    tPort = "135, 445, 5050, 8080, 80".split(", ")
    if (tHost == None) | (tPort == None):
        print(parser.usage)
        exit(0)
    else:
        portScan(tHost, tPort)