f1=open("D:\\python\\luminar\\datasets\\all_students.txt")

f2=open("D:\\python\\luminar\\datasets\\failed.txt")

# all_students=[]

# failed=[]

# for names in f1:

#     all_students.append(names.rstrip("\n"))

# for name in f2:

#     failed.append(name.rstrip("\n"))

# passed=[names for names in all_students if names not in failed]

# print(passed)

#OR

all_student=set()

fail=set()

for names in f1:

    names=names.rstrip("\n")

    all_student.add(names)

for name in f2:

    name=name.rstrip("\n")

    fail.add(name)

passed1=all_student.difference(fail)

print(passed1)