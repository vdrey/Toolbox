#find fibonacci

print('This will find fibonacci numbers')
input()

#[1, 2, 3, 5,...]
#[a, x, y, z,...]

z = 5
y = 3
x = 2
terms = [1,2,3,]

while z <= 4000000:

    if z + y > 4000000: #to find nth term, use a len statement
        print('that is it!')
        print(terms)
        break

    else:
        terms.append(z)
        a = x
        b = y
        c = z
        z = b + c
        y = b + a
        x = b
        print(terms)
