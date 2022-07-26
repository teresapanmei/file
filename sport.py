# Q9. Accept five sports names from the user and write in a file “sport.txt” (each name should write in separate line)

# Hide Answer
# Ans
f = open("sport.txt","w")
for i in range(3):
       n = input("Enter sport name:")
       f.write(n)
       f.write('\n')
f.close()