# Q8. Accept five names from the user and write in a file “name.txt”

# f = open("name.txt","w")
# for i in range(5):
#    n = input("Enter name")
#    f.write(n)
# f.close()

f = open("name.txt","w")
i=0
while i<4:
    a=input("enter any name:")
    f.write(a)
    i+=1
f.close()
