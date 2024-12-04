string="Hello"

reversed_string=''

length=len(string)-1 #len(string)-1 because while calculating length it starts from 1 whereas for indexing,it starts from 0.Here we want 0 to 4 but length returns 5(ie 1 to 5).

for i in range(length,-1,-1):

    reversed_string=reversed_string+string[i]

print(reversed_string)


