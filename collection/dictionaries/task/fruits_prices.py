fruits=["Apple","Orange","Grapes","Watermelon"]

prices=[20,30,40,50]

fruits_price={fruits[index]:prices[index] for index in range(0,len(fruits))}

print(fruits_price)