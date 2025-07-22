from utils import scan_port
import socket

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
    found_open = False

    for port in range(start_port, end_port + 1):
        if scan_port(target, port):
            found_open = True
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"
            print(f"Port {port} is OPEN ({service})")

    if not found_open:
        print("No open ports found in that range.")

print("Exiting scanner. Goodbye!")