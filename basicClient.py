import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto("Hello".encode(), ('10.95.4.115', 5000))
