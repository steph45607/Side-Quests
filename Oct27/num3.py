def prime(n):
    if n == 1 or n == 11 or n < 10: # false if 1 / 11 / one digit
        return False

    score = 0 # to check prime, if more than 2, not prime
    for i in range(1,n+1):
        if n % i == 0:
            score += 1

    if score == 2:
        return True
    return False

def emirp(n): 
    if prime(n) == False:
        return False

    r = 0 #reversing n
    while n != 0:
        d = n % 10
        r = r * 10 + d
        n = int(n/10)
    
    return prime(r)

def emripCheck(n):
    if prime(n) and emirp(n): 
        r = 0 #reversing n again, so can print r
        c = n
        while c != 0:
            d = c % 10
            r = r * 10 + d
            c = int(c/10)
        print(n," ",r)

    else:
        print("False!")

