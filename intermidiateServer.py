import sys
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('10.95.4.115', 5000))

while True:
    data,addr = sock.recvfrom(200)
    print("Server is received data:", data.decode())
    print("Send Client IP:", addr[0])
    print("Send Client Port:", addr[1])
    print("Server return data to", addr[0])

    if data.decode() == 'exit' :
        print('done')
        sys.exit()
