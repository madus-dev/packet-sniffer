import socket



HOST = socket.gethostbyname(socket.gethostname())
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind((HOST, 80))
while True:

    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

 
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)


    (data,addr) = s.recvfrom(65565)
    print(str(data.decode('utf-8', 'ignore')),addr)


    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
