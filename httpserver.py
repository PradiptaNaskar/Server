import socket

def get_ip_address(host):
    """Resolve the IP address of the given host."""
    try:
        ip_address = socket.gethostbyname(host)
        return ip_address
    except socket.gaierror as e:
        print(f"Error resolving IP address: {e}")
        return None

def connect_to_server(ip, port):
    """Connect to the web server and send/receive data."""
    try:
        # Create a TCP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to the server
        client_socket.connect((ip, port))
        
        # Formulate an HTTP GET request
        request = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(host)
        
        # Send the request
        client_socket.sendall(request.encode())
        
        # Receive the response
        response = b""
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            response += data
        
        print("Received from server:")
        print(response.decode())

        # Close the socket connection
        client_socket.close()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    host = input("Enter the hostname (e.g., www.example.com): ")
    port = 80  # Default HTTP port
    
    ip_address = get_ip_address(host)
    
    if ip_address:
        print(f"Resolved IP address for {host}: {ip_address}")
        connect_to_server(ip_address, port)
    else:
        print("Failed to resolve the IP address.")
