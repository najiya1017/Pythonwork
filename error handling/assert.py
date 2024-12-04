def voting(age):

    assert age>18,"NOT ABLE TO VOTE"

    print("voted")

def rating(rate):

    assert rate>0,"too low"

    assert rate<10,"too high"

    print("DONE")

try:

    rating(9)

except Exception as e:

    print(e)