from json import load

f=open("D:\\python\\luminar\\datasets\\datasets_json\\employee.json")

data=load(f)

for emp in data:

    print(emp)