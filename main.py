from utils import scan_port, validate_target, validate_ports
import socket
import threading

#Main loop. Enter the target, start port, and end port to begin scan.
while True:
    target = input("\nEnter the target IP or domain. To quit, enter 'exit': ")
    if target.lower() == "exit":
        break
    
    if not validate_target(target):
        print("Invalid target. Please enter a valid IP address or domain name.")
        continue
    
    ports = validate_ports(input("Enter start port: "), input("Enter end port: "))
    if not ports:
        continue

    start_port, end_port = ports

    #Header to display when scanning.
    print("\n" + "=" * 40)
    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")
    print("=" * 40 + "\n")

    threads = []
    open_ports = []

    #Threaded scan function that creates a thread for each port in the given range.
    def threaded_scan(ip, port):
        if scan_port(ip, port):
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"
            open_ports.append((port, service))

    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=threaded_scan, args=(target, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    #Display results.
    if open_ports:
        print("Open Ports Found:\n")
        for port, service in sorted(open_ports):
            print(f"  • Port {port:<5} ({service})")

    else:
        print("No open ports found in that range.")

    print("\n" + "=" * 40 + "\n")

print("Exiting scanner. Goodbye!")