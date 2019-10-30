import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while True:
    data = input("input data = ");
    sock.sendto(data.encode(), ('10.95.4.115', 5000))
    data, addr = sock.recvfrom(200)
    print("Client send and received data:", data.decode())
    print("Data from IP:", addr[0])
    print("Data from Port:", addr[1])
