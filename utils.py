import socket
import ipaddress
import re

def validate_target(target):
    try:
        ipaddress.ip_address(target)
        return True
    except ValueError:
        pass

    domain_pattern = r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.[A-Za-z]{2,6}$"
    if re.match(domain_pattern, target):
        return True
    
    return False

def validate_ports(start_port, end_port):
    try:
        start_port = int(start_port)
        end_port = int(end_port)

        if not (1 <= start_port <= 65535 and 1 <= end_port <= 65535):
            raise ValueError("Ports must be between 1 and 65535.")
        if start_port > end_port:
            raise ValueError("Start port must be less than or equal to end port.")
        
        return start_port, end_port
    
    except ValueError as e:
        print(f"Invalid port input: {e}")
        return None

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except Exception:
        return False