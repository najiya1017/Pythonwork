arr=[1,2,3,2,4,1,5,3,2,4,5,5]

counted=[]

for i in arr:

    element=i
    
    if element not in counted:

        count=0

        for j in arr:

            if i==j:

                count+=1
        
        counted.append(element)
        print(f"count of {element}={count}")

#OR

