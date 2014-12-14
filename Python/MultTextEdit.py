from random import randint

lines = 10000
docs = 0
holder = randint(1001,1100)
title = int(holder)
n = 0

while docs < 1000:
    
    with open(str(title)+".txt", "wt") as out_file:

        while n <= lines:

            if n == lines:
                n = 0
                break
            
            else:
                out_file.write("Test\n")
                n = n + 1

    
            

        docs = docs + 1
        title = title + 1
        
