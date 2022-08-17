#Wap in python to find the sum of series 1/1 , 1/2 , 1/3 , .....1/n 

def summ(n):
    sumn = 0
    while n > 0:
        sumn += 1/n
        n -= 1 
    return sumn

n = int(input("Enter a no : "))
if n == 0:
    print("not defined")
else:
    print(summ(n))




def summ(n):
    if n == 0:
        return 0
    return 1/n + summ(n-1)
    
n = int(input("Enter a no : "))
if n == 0:
    print("not defined")
else:
    print(summ(n))