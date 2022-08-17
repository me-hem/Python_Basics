#Find average of marks using fnction and list.

l = list(map(int , input().split()))
def avg(l):
    '''summ = 0
    for i in l:
        summ += i
    average = summ/len(l)
    return average'''
    
    return sum(l)/len(l)

print(avg(l))
    