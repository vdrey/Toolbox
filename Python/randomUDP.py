import socket
import random
from randLocalIP import randLocalIP


def sendPkt(): 
    UDP_IP= str(randLocalIP())
    UDP_PORT= random.randint(0,12345)
    MESSAGE= "Hello world! This a test!"
 
 
    print("UDP target IP:", UDP_IP)
    print("UDP target port:", UDP_PORT)
    print("message:", MESSAGE)
 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))

    
while True:
    sendPkt()
