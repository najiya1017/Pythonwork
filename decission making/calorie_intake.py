age=int(input("Age:"))

height=int(input("Height:"))

weight=int(input("Weight:"))

gender=input("Gender:").lower()

if gender=='male':

    BMR=10*weight + 6.25*height -5*age +5

elif gender=='female':

    BMR=10*weight + 6.25*height -5*age -161

else:
    print("*****Enter Valid Gender***")

print("BMR:",BMR)

activity_level=int(input("""
select activity level:
        press 1 for sedentary
        press 2 for slightly active
        press 3 for moderately active
        press 4 for very active
        press 5 for extra active                     
 """))

if activity_level==1:

    calorie=BMR*1.2

elif activity_level==2:

    calorie=BMR*1.375

elif activity_level==3:

    calorie=BMR*1.55

elif activity_level==4:

    calorie=BMR*1.725

elif activity_level==5:

    calorie=BMR*1.9

else:

    print("*** SELECT VALID CHOICE FOR ACTIVITY LEVEL ***")

print("Total no.of calories you need inorder to maintain your current weight=",calorie)

target_weight=int(input("Enter weight to reduce in kg:")) #1kg=7700 kilo calories

duration=int(input("Enter Duration in weaks:"))

calorie_deficit=target_weight*7700

days=duration*7

daily_calorie_deficit=calorie_deficit/days

print("Daily Calorie Deficit:",daily_calorie_deficit)

