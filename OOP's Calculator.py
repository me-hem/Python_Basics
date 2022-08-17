#Wap in python to create basic calculator using OOPs

class calculator:
    def __init__(self , n1, n2, op):
        self.num1 = n1
        self.num2 = n2
        self.opr = op
    
    def calculate(self):
        
        dict = {'+':self.num1+self.num2,
                '-':self.num1-self.num2,
                '*':self.num1*self.num2,
                '/':self.num1/self.num2,
                '%':self.num1%self.num2,
                '**':self.num1**self.num2}
        
        if self.opr not in dict.keys():
            print("invalid operation")
        else:
            print(self.num1,self.opr,self.num2,"=",dict[self.opr])
            
num1, num2, opr = int(input("Enter num1: ")), int(input("Enter num2: ")), input("Enter operator: ")
while True:
    if (opr == '/' or opr =='%') and num2 == 0:
        print("Can't divide by zero, Enter again.")    
        num2 = int(input("Enter num2: "))
    else:
        break
calc = calculator(num1,num2,opr)
calc.calculate()




