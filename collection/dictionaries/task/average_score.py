#program to calculate the average score.

people={"rahul":23,"ram":24,"seetha":25,"reenu":15}

sum_score=sum([v for v in people.values()])

average=sum_score//len(people)

print("average:",average)
