import socket

def sendPkt(): 
    UDP_IP= "192.168.0.254"
    UDP_PORT= 5005
    MESSAGE= "Hello world! This a test!"
 
 
    #print("UDP target IP:", UDP_IP)
    #print("UDP target port:", UDP_PORT)
    #print("message:", MESSAGE)
 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))

    
while True:
    sendPkt()
