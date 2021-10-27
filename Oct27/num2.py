def diamond(w: int):
    j = w
    a = 1
    for i in range(1,(2*w)):
        if (i < j):
            n = i
            print((" "*(w-1))+("*"*(n+(n-1))))
            w -= 1
            n += 1
        elif (i == j):
            n = i
            print("*"*(n+(n-1)))
            n -= 1
        else:
            print((" "*a)+("*"*(n+(n-1))))
            a += 1
            n -= 1

diamond(3)
diamond(5)
diamond(10)
