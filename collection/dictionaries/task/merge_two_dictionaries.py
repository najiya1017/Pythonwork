#merge two dictionaries

people={"rahul":23,"ram":24,"seetha":20,"reenu":29,"sahal":30}

office={"seema":30,"joe":34,"jacob":22}

for name in office:

    people[name]=office[name]

print(people)