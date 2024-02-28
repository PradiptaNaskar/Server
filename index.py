import socket

def get_ip_address(host_name):
    """Get the IP addres of the host."""
    try:
        ip_address = socket.gethostbyname(host_name)
        return ip_address
    except socket.gaierror as e:
        print(f"Error occurred: {e}")
        return None

def connect_to_server(ip_address, port):
    """Connect to the server and send/receive data."""
    try:
        # Create a TCP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        client_socket.settimeout(10)

        # Connect to the server
        client_socket.connect((ip_address, port))
        
        # Send data to the server
        message = "Hello, Server!"
        client_socket.sendall(message.encode())
        
        # Receive data from the server
        received_data = client_socket.recv(1024).decode()
        print(f"Received from server: {received_data}")

        # Close the socket connection
        client_socket.close()

    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    host_name = '172.0.0.1'
    ip_address = get_ip_address(host_name)
    
    if ip_address:
        print(f"Resolved IP address of {host_name}: {ip_address}")
        
        port = int(input("Enter the port number to connect: "))

        connect_to_server(ip_address, port)
    else:
        print("Failed to resolve the IP address.")
