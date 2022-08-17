#Let's play with string and numbers.

#1. Number palindrome , reversing a no.
'''
num = int(input())
copy = num
rev = 0

while num > 0:
    rev = rev*10 + (num % 10)    #Formula
    num = num // 10

if rev == copy: 
    print("Palindrome.")     
else:
    print("Not Palindrome")    '''
    
    
    
#2.a- String Palindrome 
'''
string = str(input("enter the string: "))

rev = ""
for i in string:
    rev = i + rev

if rev == string: 
    print("Palindrome.")     
else:
    print("Not Palindrome") 
'''

#2.b  Common indexing method
'''string = input()
rev = ""

for i in range(len(string),0,-1):
    rev += string[i-1]

if rev == string: 
    print("Palindrome.")     
else:
    print("Not Palindrome")    '''
    


#3.a Swapping numbers in one line
'''num1, num2 = int(input()), int(input())
print("Num1: ",num1," Num2: ",num2)
num1, num2 = num2, num1
print("Num1: ",num1," Num2: ",num2)'''

#3.b Swapping number using third variable
'''num1, num2 = int(input()), int(input())
print("Num1: ",num1," Num2: ",num2)

temp = num1
num1 = num2
num2 = temp

print("Num1: ",num1," Num2: ",num2)'''

#3.c Swapping number without third variable
num1, num2 = int(input()), int(input())
print("Num1: ",num1," Num2: ",num2)

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("Num1: ",num1," Num2: ",num2)



































  