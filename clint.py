import socket

# Define server address and port
server_address = ("127.0.0.1", 12345)

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Message to send
message = "Hello SIT202"

# Send message to server
client_socket.sendto(message.encode(), server_address)

# Receive response from server
response, _ = client_socket.recvfrom(1024)
decoded_response = response.decode()

# Print the received message
print(f"Received from server: {decoded_response}")

# Close the socket
client_socket.close()
