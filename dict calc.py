#Derived data types i.e. list, dictionary, tuple, sets
#Dictionary: key-value pair
#Unique keys , keys can't be list

x , y , z = int(input("enter no 1: ")) ,int(input("enter no 2: ")) ,input("enter operator: ")


while((z == "/" or z == "%") and y==0):
    print("cant't divide by zero, enter again.")
    y = int(input("Enter no 2: "))

result = {
    "+": x+y,
    "-": x-y,
    "*": x*y,
    "/": x/y,
    "%": x%y
    }

if z in result.keys():
    print(x,z,y,"=",result[z])
else:
    print("Invalid Operation")     