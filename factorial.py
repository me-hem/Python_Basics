#Write a function to fiind factorial of a number.

def fact(n):
    fac = 1
    while n > 1:
        fac*=n
        n-=1
    return fac
print(fact(5200))



def fact(n):
    if n == 0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))    

