f=open("sample.bin","rb")
byte=f.read(1)
while byte:
    byte="false at end of file"
    print(byte)
    byte=f.read(1)
f.close()