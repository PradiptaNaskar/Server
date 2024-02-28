import socket
import threading

def check_port(host, port):
    """Check if a port is open on a host."""
    try:
        # Create a TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Set a timeout for the connection attempt
            s.settimeout(1)
            
            # Attempt to connect to the host and port
            result = s.connect_ex((host, port))
            
            # Check if the port is open
            if result == 0:
                print(f"Port {port} on {host} is OPEN.")
            else:
                print(f"Port {port} on {host} is CLOSED.")
    except Exception as e:
        print(f"An error occurred while checking port {port}: {e}")

if __name__ == "__main__":
    
    host = input("Enter the hostname or IP address to scan: ")
    
    # Get the port range from the user
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))
    
    print(f"Scanning ports {start_port} to {end_port} on host {host}...\n")
    
    # Use threading for faster scanning (each port is checked in a separate thread)
    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=check_port, args=(host, port))
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    print("\nPort scanning complete.")


