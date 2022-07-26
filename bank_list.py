# files-question3
# Aapke paas ek list hai. Iss list mein har string ko ek file-question3.txt naam ki file mein nayi line mein daalo. Aapki list yeh rahi:


# Code Example

bank_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
f=open("bank_list","w")
i=0
while i<len(bank_list):
    if bank_list[i]:
        f.write(bank_list[i]+"\n")
    i+=1
f.close

