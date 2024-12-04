for row in range(1,7): #1
    
    for space in range(1,7-row):

        print(" ",end="")

    for col in range(1,row+1):

        print("* ",end="")

    print()

for row in range(6,0,-1): #1
    
    for space in range(1,7-row):

        print(" ",end="")

    for col in range(1,row+1):

        print("* ",end="")

    print()