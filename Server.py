import socket

# Define server address and port
server_address = ("127.0.0.1", 12345)

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address
server_socket.bind(server_address)

print("UDP Server is running and waiting for messages...")

while True:
    # Receive message from client
    message, client_address = server_socket.recvfrom(1024)
    decoded_message = message.decode()

    # Count characters and convert to uppercase
    char_count = len(decoded_message)
    response_message = f"{char_count} - {decoded_message.upper()}"

    # Send response back to client
    server_socket.sendto(response_message.encode(), client_address)
    print(f"Processed message from client: {decoded_message} (Characters: {char_count})")
