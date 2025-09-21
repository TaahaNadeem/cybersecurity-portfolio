import socket
from threading import Thread

target = input("Enter target IP (e.g., 127.0.0.1): ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

open_ports = []

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    if sock.connect_ex((target, port)) == 0:
        print(f"Port {port} is OPEN")
        open_ports.append(port)
    sock.close()

threads = []

for port in range(start_port, end_port + 1):
    t = Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\nScan complete. Open ports:", open_ports)
