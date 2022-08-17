#Errors: Programmer's fault in a code
#Exceptions: Unexpected or unusal in events
#Exception handling: It is a mechanism to handle exceptions.
'''
a, b = 9, 0
try:
    print(a/b)
except ZeroDivisionError:
    print("can't divide by zero")
    raise
else:
    print(a/b)    
finally:
    print("Thanks for using calculator")'''
    
try: 
    arr = [0,1,4]
    print(arr[3])    
except LookupError:
    print("index out of bound")
finally:
    print("searching done")
   

