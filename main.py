from utils import scan_port, validate_target, validate_ports
import socket
import threading

while True:
    target = input("Enter target IP or domain or 'exit' to quit: ")
    if target.lower() == "exit":
        break
    
    if not validate_target(target):
        print("Invalid target. Please enter a valid IP address or domain name.")
        continue
    
    ports = validate_ports(input("Enter start port: "), input("Enter end port: "))
    if not ports:
        continue

    start_port, end_port = ports

    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

    threads = []
    open_ports = []

    def threaded_scan(ip, port):
        if scan_port(ip, port):
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"
            print(f"Port {port} is OPEN ({service})")
            open_ports.append(port)

    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=threaded_scan, args=(target, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    if not open_ports:
        print("No open ports found in that range.")

print("Exiting scanner. Goodbye!")