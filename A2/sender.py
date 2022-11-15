import socket

senderIP = "10.0.0.1"
senderPort   = 20001
recieverAddressPort = ("10.0.0.2", 20002)
bufferSize  = 1024 #Message Buffer Size

# Create a UDP socket at reciever side
socket_udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


while True:

    # Send to server using created UDP socket
    msg = input("Please enter message to send: ")
    message = str.encode(msg)
    socket_udp.sendto(message, recieverAddressPort)

    #wait for reply message from reciever
    msgFromServer = socket_udp.recvfrom(bufferSize)

    msgString = "Message from Server {}".format(msgFromServer[0])
    print(msgString)
