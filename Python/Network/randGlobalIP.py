# This generates a random IP
# It generates public or private (even if the private ips aren't available)

# IP address in form A.B.C.D

def globalIP():
    A = str(192)
    B = str(168)
    C = str(0)

    import random

    D = random.randint(1,256)
    D = str(D)

    Ls = [A,B,C,D]

    IP = '.'.join(Ls)

    return str(IP)

