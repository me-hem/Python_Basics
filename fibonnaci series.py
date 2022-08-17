# Fibonicci series - 0 1 1 2 3 5 8 13 21.......


'''def fib(n):
    f=0
    s=1
    if n == 0:
        print("Nothing")
    else:   
        print(0,end = " ")
        for i in range(n-1):
            f, s = s, f+s
            print(s, end=" ")            
            
fib(10)          '''  
        

def fib(n):                             #3
    if n < 2:                           #4
        return n                        #.
    else:                               #.
        return fib(n-1) + fib(n-2)
   
n = int(input())                        #function starts 1
for i in range(n):                      #2
    print(fib(i) , end = " ")
        
        
    
    