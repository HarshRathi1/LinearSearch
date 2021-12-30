def linearsearch(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            return i,True
        i+=1
    return False
list=[1,4,6,7,8,5,33,55,65,37,19,90,87,457,11524]
n=65
if linearsearch(list,n):
    print("Found",linearsearch(list,n))
else:
    print("Not found")