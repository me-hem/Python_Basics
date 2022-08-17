#WAP in python to find the log base 2 of (n) approximation

'''def log_2(n):
    if n ==1:
        return 0 
    return 1 + log_2(n//2)

n = int(input("enter a no: "))
print(log_2(n))'''


# WAP in Python to print inverted binary right angled triangle

r = int(input("no of rows: "))
bin = -1
for i in range(r ,0,-1):
    for j in range(i):
        print((bin + 1) // 2, end=" ")
        bin*= -1
    print()    
        
