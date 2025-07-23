from utils import scan_port
import socket
import threading

while True:
    target = input("Enter target IP or domain or 'exit' to quit: ")
    if target.lower() == "exit":
        break

    try:
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))
    except ValueError:
        print("Please enter valid port numbers.")
        continue

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