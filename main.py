from threading import *
import optparse
import socket
import sys
import os 

screenLock = Semaphore(value=1)
def connScan(target_host, target_port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.connect((target_host, target_port))
        s.send(b"donttmindme\r\n")
        print(f"{target_port} open")
        response = s.recv(1024)
        screenLock.acquire()
        print(response.decode())
    except:
        screenLock.acquire()
        print(f"{target_port} not open on {target_host}")
    finally:
        screenLock.release()
        s.close()

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
    socket.setdefaulttimeout(1)
    for port in ports:
        print(f"Scanning port {port}")
        t = Thread(target=connScan, args=(hostname, int(port)))
        t.start()
        #connScan(hostname, int(port))

def main():
    parser = optparse.OptionParser("[*] Usage: %prog -H '<target host>' -p '<target port>'")
    parser.add_option("-H", type="string", help="Specify Target Hostname", dest="target_host")
    parser.add_option("-p", type="string", help="Specify Target Port", dest="target_port")
    (options, args) = parser.parse_args()
    tHost = options.target_host
    tPort = str(options.target_port).split(', ')
    if (tHost == None) | (tPort == None):
        print(parser.usage)
        exit(0)
    portScan(tHost, tPort)

if __name__ == "__main__":
    main()