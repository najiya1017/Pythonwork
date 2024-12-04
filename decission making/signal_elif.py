# Syntax

# if condition:
#     stmt

# elif condition2:
#     stmt 

# elif condition3:
#     stmt 

# else:
#     stmt

signal=input("Signal=")

if signal=="red" or signal=="Red":
    print("STOP")

elif signal=="green" or signal=="Green":
    print("GO")

elif signal=="yellow" or signal=="Yellow":
    print("WAIT")

else:
    print("Invalid Syntax")
    
    #or

signal=input("Signal=").lower()

if signal=="red":
    print("STOP")

elif signal=="green":
    print("GO")

elif signal=="yellow":
    print("WAIT")

else:
    print("Invalid Syntax")