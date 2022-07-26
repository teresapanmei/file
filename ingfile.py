f=open("ingfile.txt","r")
count=0
a=f.read()
b=a.split()
for i in b:
    if "ing" in i:
        count+=1
print(count)

# f=open("ingfile.txt","r")
# count=0
# a=f.read()
# b=a.split()
# i=0
# while i<len(f):
#     if "ing" in f:
#         count+=1
# print(count)