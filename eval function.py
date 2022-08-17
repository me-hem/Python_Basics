#functions: inbuilt and user-defined
#inbuilt functions

expr = input("Enter expression to compute: ")
while ("/" in expr or "%" in expr):
    if (expr[expr.index("/")+1] == "0") or (expr[expr.index("%")+1] == "0"):
        print("Invalid expression, enter again.")
        expr = input("Enter expression to compute: ")
    else:
        print(eval(expr))
        break