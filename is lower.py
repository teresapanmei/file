lower_case=0
f=open("is lower.txt","r")
live=f.read()
for i in live:
    if (i.islower()==True):
        lower_case+=1
print("total no. of lower_case is",lower_case)

