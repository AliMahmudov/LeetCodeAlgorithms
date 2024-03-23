
num=int(input("enter the number: "))
t=int(input("enter the number of operations: "))

def findTheAchiaveableMax(num,t):
    if t<num:
        min_value=t
    max_increment=min_value*2
    max_achievable_number=num+max_increment
    

findTheAchiaveableMax(num,t)

 