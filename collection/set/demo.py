#set defined by set()

st=set()

#duplicates not allowed

st={10,20,30,10,20,30}

print(st)

#insertion order not preserved

st={10,20,30,10,20,30,"hello","hai",True}

print(st)

#add()==> to insert object to set

colors={"red","blue","green"}

colors.add("yellow")

print(colors)

#intersection()==> intersect two sets

st1={1,2,3,4,5}

st2={2,4,5,6,7,8}

st3={1,2,3}

intersect=st1.intersection(st2)

print(intersect)

#union()==> include elements of both sets

union=st1.union(st2)

print(union)

#difference==> removes elements which is common to both set

difference=st1.difference(st2)

print(difference)

#remove==> removes element from the set

st2.remove(5)

print(st2)

#issubset(mainset)==> returns true if the given set is subset of main set

print(st1.issubset(st2))

print(st3.issubset(st1))

#issuperset(subset)==>returns true if the given set is superset of subset

print(st1.issuperset(st3))

#symmetric_difference()==>symmetric difference means first take union of both set then remove the common of both sets

symmetric_difference=st1.symmetric_difference(st2)

print(symmetric_difference)

#update=update set1 elements with set2

st1.update(st2)

print(st1)