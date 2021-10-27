def diamond(w: int):
    j = w # j to measure i
    a = 1 # for the reverse
    for i in range(1,(2*w)):
        if (i < j):
            n = i # n for number of starts
            print((" "*(w-1))+("*"*(n+(n-1))))
            w -= 1
            n += 1 # increase with i
        elif (i == j):
            n = i
            print("*"*(n+(n-1)))
            n -= 1 # to begin reverse
        else:
            print((" "*a)+("*"*(n+(n-1))))
            a += 1 # for the amount of spaces before *
            n -= 1

diamond(3)
diamond(5)
diamond(10)
