#Understanding derived data types i.e. list, dictionaries, tuple, set

#list : contiguous memory allocation
l =  [12, 23, " Apple"]

for i in range(3):
    l.append(input(" Enter Element: "))
    
l[0] = "changed"    
l.remove('hdffg')
l.sort()
l.reverse()
print(l) 
