def print_mobile_data(**kwargs):

    print(kwargs.get("name"))

    print(kwargs.get("price"))

# print_mobile_data(name="oneplus",price=35000,display="amoled")


def calculator(*args,**kwargs):

    if kwargs.get("operation")=="+":

        return sum(args)

    if kwargs.get("operation")=="*":

        result=1

        for num in args:

            result=result*num

        return result


# print(calculator(10,20,30,operation="*"))

def student_info(*args,**kwargs):

    if kwargs.get("operation")=="avg":

        average=sum(args)/len(args)

        return average

    if kwargs.get("operation")=="total":

        return sum(args)

# print(student_info(45,43,47,operation="avg"))

# print(student_info(45,43,47,47,50,operation="total"))

def sort_numbers(*args,**kwargs):

    if kwargs.get("reverse")==True:

        return sorted(args,reverse=True)

    if kwargs.get("reverse")==False:

        return sorted(args)

print(sort_numbers(20,60,45,20,100,reverse=True))

print(sort_numbers(20,60,45,20,100,reverse=False))

