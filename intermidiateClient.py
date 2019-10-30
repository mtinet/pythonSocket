import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while True:
    data = input("input data = ");
    sock.sendto(data.encode(), ('10.95.4.115', 5000))
