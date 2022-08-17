#Function returning function

'''def func(n):
    return lambda a: a*n

double = func(2)    #passing value of n
triple = func(3)

print(double(11))   #passing value of a 
print(triple(11))'''



# Recursion

def add(n):
    if n == 0:
        return 0
    else:
        return n + add(n-1)
print(add(10))    