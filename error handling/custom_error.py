def review(rating):

    if rating<0:

        raise Exception("TOO LOW")

    elif rating>10:

        raise Exception("TOO HIGH")

    else:

        print("DONE!!!")

try:

    review(19)

except Exception as e:

    print(e)