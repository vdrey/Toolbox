# This generates a random IP on a 192.168.0.0/24 subnet


# IP address in form A.B.C.D

def randLocalIP():
    A = str(192)
    B = str(168)
    C = str(0)

    import random

    D = random.randint(1,256)
    D = str(D)

    Ls = [A,B,C,D]

    IP = '.'.join(Ls)

    return IP
