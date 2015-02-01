# This generates a random IP
# It generates public or private (even if the private ips aren't available)

# IP address in form A.B.C.D
import random

def randOct(x,y):
    return str(random.randint(x,y)


def globalIP():
    A = str(192)
    B = str(168)
    C = str(0)

    
    D = random.randint(1,256)
    D = str(D)

    Ls = [A,B,C,D]

    IP = '.'.join(Ls)

    return str(IP)

