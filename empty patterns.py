#WAP IN PYTHON TO PRINT SQUARE

n = int(input("enter the length: "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1:
            print("*",end=" ")
        elif j == 0 or j==n-1:    
            print("*",end=" ")
        else:    
            print(" ",end=" ")
    print()


#WAP IN PYTHON TO PRINT EMPTY TRIANGLE

n = int(input())

for i in range(n):
    for j in range(i+1):
        if i == n-1:
            print("*" , end = " ")
            
        elif j == 0 or j == i:
            print("*" , end = " ")
            
        else:
            print(" " , end = " ")
        
    print()

# WAP IN PYTHON TO PRINT EMPTY INVERTED TRIANGLE 

n = int(input())

for i in range(n , 0 , -1):
    for j in range(i):
        if i == n:
            print("*",end = " ")
            
        elif j == i-1 or j == 0:
            print("*" , end = " ")
            
        else:
            print(" ", end = " ")
            
    print()
            
            
            
 
# WAP IN PYTHON TO PRINT EMPTY INVERTED BINARY TRIANGLE

n = int(input())

Bin = -1

for i in range(n , 0 , -1):
    for j in range(i):
        if i == n :
            print((1-Bin)//2 , end = " ")
        
        elif j == 0 or j == i - 1 :
            print((1-Bin)//2, end = " ")
            
        else:
            print(" " , end = " ")
        
        Bin *= -1
    print()
        
            
            
            
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            





