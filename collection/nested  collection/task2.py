student_data={
    "hari":[45,40,35],
    "vipin":[34,40,45],
    "vinay":[45,40,35],
    "bijoy":[33,38,35],
    "anvin":[32,3040]
}

avg_mark={k:sum(v)/len(v) for k,v in student_data.items()}

# for i,element in enumerate(student_data):

#     marks=student_data.get(element)

#     avg=sum(marks)/len(marks)

#     avg_mark[element]=avg

print(avg_mark)        


    