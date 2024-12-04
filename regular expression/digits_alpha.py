from re import finditer

text="I have 3 cars,2 bike,1 Cycle"

pattern="[a-z]"

pattern2="[0-9]"

pattern3="[a-zA-Z0-9]"

pattern4="[^ak]" 

pattern5="[b-jl-z]"

pattern6="[^a-zA-Z0-9]"

matcher=finditer(pattern,text) #checks for lowecase alphabets

matcher2=finditer(pattern2,text) #checks for digits

matcher3=finditer(pattern3,text) #checks for lowercase,upper case alphabets and digits

matcher4=finditer(pattern4,text) #only excludes a,k from the text,prints special character

matcher5=finditer(pattern5,text) #print lower case alphabets excluding a,k

matcher6=finditer(pattern6,text) #print special characters

for obj in matcher6:

    print(obj.start(),"==>",obj.group())