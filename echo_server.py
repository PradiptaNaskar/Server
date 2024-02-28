import socket

def start_echo_server(port):
    """Start a simple echo server."""
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the port
    server_socket.bind(('localhost', port))
    
    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Echo server listening on port {port}...")
    
    while True:
        # Accept incoming connection
        client_socket, address = server_socket.accept()
        print(f"Connection from {address}")
        
        # Receive data from client
        data = client_socket.recv(1024)
        
        if data:
            print(f"Received data: {data.decode()}")
            
            # Echo back the received data
            client_socket.sendall(data)
        
        # Close client connection
        client_socket.close()

if __name__ == "__main__":
    PORT = 12345  # You can choose any available port number
    start_echo_server(PORT)
