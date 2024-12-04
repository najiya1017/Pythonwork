cars=[
    {"id":1,"name":"fronx","price":1200000,"brand":"nexa","colors":["red","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":2,"name":"baleno","price":1100000,"brand":"nexa","colors":["grey","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":3,"name":"3xo","price":900000,"brand":"mahindra","colors":["red","white","black"],"transmissions":["amt","cvt"]},
    {"id":4,"name":"punch","price":700000,"brand":"tata","colors":["red","blue","green","white"],"transmissions":["manuel","cvt"]},
    {"id":5,"name":"nexon","price":1400000,"brand":"tata","colors":["red","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":6,"name":"kiger","price":1000000,"brand":"renault","colors":["blue","white"],"transmissions":["manuel","cvt","dct"]},
    {"id":7,"name":"taigun","price":2300000,"brand":"volkswagon","colors":["red","blue","white"],"transmissions":["manuel","cvt","torqe"]},
]

#total no.of vehicles

print(f"Total no.of cars:{len(cars)}")

#print available color of cars

available_colors=[c.get("colors") for c in cars if c.get("name")=="baleno"] #returns [['grey', 'blue', 'white']]
                                                                                            #0
print(available_colors[0]) #returns ['grey', 'blue', 'white']

#print brands without duplicates

brands=set([c.get("brand") for c in cars]) #OR brands={c.get("brand") for c in cars},set comprehension

print(brands)

#print car names available in amt transmission

transmissions=[c.get("name") for c in cars if "amt" in c.get("transmissions")]

print(transmissions)

#cars available in blue colors

bue_color=[c.get("name") for c in cars if "blue" in c.get("colors")]

print(bue_color)

#print all transmission type

transmission_type={t for c in cars for t in c.get("transmissions")}

print(transmission_type)

#print all colors

all_colors={cl for c in cars for cl in c.get("colors")}

print(all_colors)

#most popular color

all_clr=[color for c in cars for color in c.get("colors")]

grp={clr:all_clr.count(clr) for clr in all_clr}

print(max(grp,key=lambda c:grp.get(c)))

#costly car

costly_car={c.get("name"):c.get("price") for c in cars }

print(max(costly_car,key=lambda c:costly_car.get(c))) #OR max(cars,key=lambda d:d.get("price")),print(costly_car.get("name"))

#car with minimum cost

print(min(costly_car,key=lambda c:costly_car.get(c))) #OR min(cars,key=lambda d:d.get("price")),print(costly_car.get("name"))

#sort cars wrt price

print(sorted(costly_car,key=lambda c:costly_car.get(c),reverse=True)) 

#OR 

sorted_dictionary=sorted(cars,key=lambda d:d.get("price"))

print({c.get("name"):[c.get("price"),c.get("brand")] for c in sorted_dictionary}) #returns values in list.