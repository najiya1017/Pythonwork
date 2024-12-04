employee={"eid":1000,
            "name":"rahul",
            "salary":50000,
            "department":"developer",
            "experience":6
          }

employee["contact"]=3456789

""""

if experience>5,add 10000 to current salary
else add 5000 to current salary

"""

if employee["experience"]>5:

    employee["salary"]+=10000

else:

    employee["salary"]+=5000

#add role as SDE if exp>5 else JDE

if employee["experience"]>5:

    employee["role"]="SDE"

else:

    employee["role"]="JDE"

print(employee) 