#Derived data types i.e. list, dictionary, tuple, sets
#Dictionary: key-value pair
#Unique keys , keys can't be list

x , y = int(input("enter no 1: ")) ,int(input("enter no 2: "))
z = input("enter operator: ")
result = {
    "+": x+y,
    "-": x-y,
    "*": x*y,
    "/": x/y,
    "%": x%y
    }



if z in result.keys() or not((z == "/" or z == "%") and y==0):
    print(x,z,y,"=",result[z])
else:
    print("Invalid Operation")    