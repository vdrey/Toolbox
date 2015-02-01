# This generates a random IP
# It generates public or private (even if the private ips aren't available)

# IP address in form A.B.C.D
import random

def randOct(x,y): # X and Y are the starting/ending integers of the range
                  # default should be (1,256) for A & D and (0,256) for C & B 
    x = int(x)
    y = int(y)
    return str(random.randint(x,y)


def globalIP():
               
    A = str(randOct(1,256))
    B = str(randOct(0,256))
    C = str(randOct(0,256))
    D = str(randOct(1,256))

    Ls = [A,B,C,D]

    IP = '.'.join(Ls)

    return str(IP)

