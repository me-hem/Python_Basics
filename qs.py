#Armstrong number : 364 = 3^3 + 6^3 +4^3

def check_A0(n):
    sum = 0
    l=len(str(n))
    fin = n
    while n > 0:
        sum += (n%10) ** l
        n //= 10
    return sum == fin
if(check_A0(153)):
    print("Armstrong number.")
else:
    print("Not an Armstrong number.")
    

def check_A0(n,l):
    if n == 0:
        return 0
    return (n%10)**l + check_A0(n//10,l)

num = int(input("enter a no.: "))

if check_A0(num,len(str(num))) == num:
    print("Armstrong number.")
else:
    print("Not an Armstrong number.")
