#Procedural Programming                 #top down approach
#->Focus on procedures or functions not on data.

#OOP - Object Oriented Programming      #bottom up approach
#->Focus on manipulating and organising data

#-> Object: Real world entity (Instance of a class)
#Entity having a state (data members) and a behaviour(member functions) associated with it.

#-> Class: User-defined data-type / Blueprint for the objects / Collection of objects

                        
                        #Pillars of OOPs

#->Data Abstraction: Highlighting only useful data.
#   ->>Access specifiers i.e. Public, Protected, Private
#       ->>>Public: Accessible inside the class and outside too. Can be inherited.
#       ->>>Protected: Accessible inside the class and but not outside. Can be inherited.
#       ->>>Private: Accessible inside the class and but not outside. Can't be inherited.
'''
class student:
    #Data members / State
    __roll = 0 #__ ->private(2 underscores __)
    _name = None #_ ->protected(1 underscore _)
    marks = 0  # ->public(No underscore)

s = student()   # s is object of class student

print(s.marks)  # accessible both inside and outside class as it is public data member
print(s.__roll) # error as it is private data member.
print(s._name)  # error as it is protected data member.
'''

#->Encapsulation
#   ->>Binding up of state and behaviour of an object in a single entity.
#   ->>Binding up of data members and associated functions into a single entity.
'''
class student:
    #Data members / State
    __roll = 0
    __name = None
    __marks = 0 

#   ->>Constructor: Special function which is used to initialise the values of object at the time of object creation.
    #Member functions / Behaviour
    def __init__(self, __name, __roll, __marks):
        self.__name = __name
        self.__roll = __roll
        self.__marks = __marks
        print("Contructor is called, means Object created...")
        
#   ->>Destructor: Special function which is used to delete the memory of object when it goes out of scope.   
    def __del__(self):
        print("Destructor is called, means object destroyed...")
        
    def percentage(self):
        print(self.__name,",you have got ",self.__marks/5,"%" , sep = "")
if __name__ == "__main__":
    s = student("Udit",2043,478)
    s1 = student("Umesh",53,500)
    s.percentage()
    s1.percentage()
'''


#--->>>Keywords: These are some reserved words which have some special meaning to language compiler.
#--->>>Identifiers: These are the names given to variables, functions etc. by programmer.

#->Inheritance
#It is the capability of a classs to inherit properties from base/parent/super class
#Represents real world relationships.
#Code reusability
'''
class car:
    def __init__(self,name):
        self.company_name = name
    def getcompany(self): #Accessor function - we acessed private __company_name
        #return self.__company_name
        print(self.company_name)
    def is_on_trend(self):
        return False
    
class ferrari(car): #ferrari is a child class of car.
    def __init__(self,model, name):
        super().__init__(name)
        self.model_no = model
    def is_on_trend(self):
        return True           
    
c = ferrari("Fer0232","Ferrari")    #c is an object of sub class ferrari
c.getcompany()  # **INHERITANCE** ->> we accessed getcompany() of super class from the object of child class(c).

print("It is on trend: ",c.is_on_trend())  #Method over-riding  
'''

#Types of Iinheritance:    
#   ->Single Inheritance
        # ->> Let A be the super class, B is derived from A.
      
#   ->Multilevel Inheritance
        #->>Let A be the super class, B is derived from A and further C is derived from B.
        
#   ->Multiple Inheritance
        #->>Let A and B be the super class, C is derived from A and B.
        
#   ->Heirarical Inheritance
        #->>Let A be the super class, B is derived from A and C is also derived from A.
        
#   ->Hybrid Inheritance
        #->>Let A and B be the super classes and C is derived from A and B, Futher D and E are derived from C.
        #->>Dreaded Diamond: Let A be the super class and B and C are derived from A, Further D is derived from B and C.

#->Modularity: Break down of large code into small small modules to decrease the complexity of the code and to make debugging easier.


#->Polymorphism
        #->>Poly - Many , Morphism - States
        #->>Ability of an object to behave differently in different states.
        #->>How to achieve polymorphism? - By creating different methods of same name but different signatures.
        #->>Types of polymorphism: 
            #(:-Compile-time polymorphism(Overloading)-polymorphism at compilation time
                #(:=> Overloading: Creating functions with same name but different signatures within the same class.
                    #python does not support method overloading by default.        
'''
class shape:
    def __init__(self):
        self.a = 0
                    
    def area(self, side):
        self.a = side**2
        return self.a
#In case of overloading in python, the latest function definition overwrites the old definitions.
                
    def area(self, length, breadth):
        self.a = length*breadth
        return self.a
                    
var = shape()   #var is the object of class shape
print(var.area(2))
'''

             #(:=> Overriding: Creating function with same name and same signature in derived class which is already present in base class.       
'''
class car:
    def __init__(self,name):
        self.company_name = name
    def getcompany(self): #Accessor function - we acessed private __company_name
        #return self.__company_name
        print(self.company_name)
    def is_on_trend(self):
        return False
    
class ferrari(car): #ferrari is a child class of car.
    def __init__(self,model, name):
        super().__init__(name)
        self.model_no = model
    def is_on_trend(self):
        return True           
    
c = ferrari("Fer0232","Ferrari")    #c is an object of sub class ferrari
c.getcompany()  # **INHERITANCE** ->> we accessed getcompany() of super class from the object of child class(c).

print("It is on trend: ",c.is_on_trend())  #Method over-riding  
                    
        