import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('10.95.4.115', 5000))
data, addr = sock.recvfrom(200)

print("Server is received data:", data.decode())
print("Send Client IP:", addr[0])
print("Send Client Port:", addr[1])
