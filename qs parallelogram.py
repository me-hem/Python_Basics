'''def no(a):
    print(a)
    if a == n:
        return    
    return no(a+1)

a = 1
n = int(input())
no(a)'''


# Print rhombus and parallelogram both empty and filled

'''n = int(input())
for i in range(n):
ṇ    print(" "*(n-i)+" *"*(n+1))'''
    

'''r , c= int(input()), int(input())
for i in range(r):
    k=0
    for j in range(c):
        while k < r-i:
            print(" ",end=" ")
            k+=1            
        print("*",end=" ")
    print()   '''
    
    
# Empty parallelogram

"""r , c= int(input()), int(input())

for i in range(r):
    k = 0
    for j in range(c):
        while k < r-i:
            print(" " , end = " ")
            k += 1
            
        if i == 0 or i == r-1:
            print("*" , end = " ")
        
        elif j == 0 or j == c-1 :
            print("*" , end = " ")
        
        else :
            print(" " , end = " ")
                
    print()"""
        

# Print 2-d Pyramid

'''n = int(input("Enter the length of side: "))

for i in range(1, n+1):
    k=0
    for j in range(0,n-i):
        print(" ", end=" ")
    while k<(2*i-1):
        print("*", end=" ")
        k+=1
    print()'''


# Empty Pyramid

'''n = int(input("Enter the length of side: "))

for i in range(1, n+1):

    for j in range(0,n-i):
        print(" ", end=" ")
        
    for k in range(j+1,2*n):
        if i == n:
            print("*", end=" ")
            
        elif k == (n*2-1)//2-i+1 or k == (n*2-1)//2+i-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
    
# OR

# Generating Hollow Pyramid Pattern Using Stars

'''row = int(input('Enter number of rows required: '))

for i in range(row):
    for j in range(row-i):
        print(' ', end=' ') # printing space required and staying in same line
    
    for j in range(2*i+1):
        if j==0 or j==2*i or i==row-1:
            print('*',end=' ')
        else:
            print(' ', end=' ')
    print() # printing new line
'''

str = "A"
n = int(input())
for i in range(n):
    for j in range(i+1):
        print(str , end = " ")
    str = chr(ord(str)+1)     # 
    print()
    
  






















