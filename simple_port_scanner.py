import socket

# Get target from user
target = input("Enter the IP address or hostname to scan: ")

# Get port range
start_port = int(input("Enter the starting port number: "))
end_port = int(input("Enter the ending port number: "))

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)  # short timeout for faster scanning
    try:
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")
    except Exception as e:
        print(f"Port {port}: ERROR ({e})")
    finally:
        s.close()

print("\nScan complete.")