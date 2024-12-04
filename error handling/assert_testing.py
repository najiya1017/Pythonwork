def is_leap_year(year):

    if year<0:

        return False

    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:

        return True

    else:

        return False

def test_is_leap_year():

    assert is_leap_year(2024)==True,"leap year check failed"

    assert is_leap_year(2022)==False,"invalid leap year check failed"

    assert is_leap_year(2000)==True,"valid century leap year check failed" 

    assert is_leap_year(1900)==False,"invalid century leap year check failed"

    assert is_leap_year(-1900)==False,"-ve invalid leap year check failed"

    assert is_leap_year(-2000)==False,"-ve with valid leap year check failed "


# print(is_leap_year(1900))

try:

    test_is_leap_year()

    print("test success")

except Exception as e:

    print(e)




