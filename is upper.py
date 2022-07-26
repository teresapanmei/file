# upper_case=0
# f=open("is upper.txt","r")
# live=f.read()
# for i in live:
#     if (i.isupper()==True):
#         upper_case+=1
# print("total no. of lower_case is",upper_case)

upper_case=0
f=open("is upper.txt","r")
live=f.read()
i=0
while i>len(live):
    if (i.isupper()==True):
        upper_case+=1
    i+=1
print("total no. of upper_case is",upper_case)
f.close()