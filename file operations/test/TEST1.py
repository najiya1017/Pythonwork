f=open("D:\\python\\luminar\\datasets\\test\\sample.txt","w")

message=input("Write something:")

f.write(message+"\n")

f.close()

f_read=open("D:\\python\\luminar\\datasets\\test\\sample.txt")

for message in f_read:

    print(message)
    
f_read.close()