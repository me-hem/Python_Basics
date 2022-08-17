#Functions in python
#User-defined function

#global  - scope throughout the programm , defined outside the function, here x and y  

'''x = int(input("enter no 1: "))
y = int(input("enter no 2: "))
def sum():
    summ = x + y  # this is local
    return summ
print(sum())'''
    



'''x = int(input("enter no 1: "))
y = int(input("enter no 2: "))

def sum(x , y):  #we pass value in argument
    summ = x + y
    return summ

print(sum(x , y))'''



x = int(input())
y = int(input())

def change(x , y):
    x*=10
    y-=12
    
change(x,y)
print(x, y)    
    
    