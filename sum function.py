#Find sum of first n-natural numbers using functions.

n = int(input())
'''def summ(n):
    summm = 0
    for i in range(1 , n+1):
        summm += i
    
   return summm

print(summ(n))

def sumn(n):
    return n*(n+1)//2
print(sumn(n))'''


# lambda is a short hand notation for function ....
    
result = lambda n: n*(n+1)//2
print(result)

area = lambda a,b: a*b
print(area(4,5))
