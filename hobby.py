# Q10. Accept five hobbies from the user and write in a file “hobby.txt” (each hobby should write in separate line) without using write() function.


# f = open("hobby.txt","w")
# h = [ ]
# for i in range(5):
#        n = input("Enter hobby name")
#        h.append(n,\
# f.writelines(h)
# f.close()

f=open('hobby.txt','w')
h=[]
i=0
while i<5:
       n=input("enter your name")
       h.append(n)
       h.append("\n")
       i+=1
f.writelines(h)
f.close()