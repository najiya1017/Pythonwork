# 13. Roman to Integer
# Lasy
# • Topics
# à Companies
# ® Hint
# Roman numerals are represented by seven different symbols: I, v. X, L. C. D and M.
# Symbol
# Value
# V
# X
# L
# 5
# 10
# 50
# 100
# 500
# 1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply x + II. The number 27 is written as XXVII, which is XX + v + II.
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
# • I can be placed before v (5) and x (10) to make 4 and 9.
# • x can be placed before L (50) and c (100) to make 40 and 90.
# • C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

roman=input("Roman:")
roman=list(roman) #["I","V"]
symbol={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
val=0
skip=False
for i in range(len(roman)):
    if skip==True:
        skip=False
        continue
    if i!=len(roman)-1 and symbol.get(roman[i])<symbol.get(roman[i+1]):
        difference=symbol.get(roman[i+1])-symbol.get(roman[i])
        val=val+difference
        i=i+1
        skip=True
    else:
        val=val+symbol.get(roman[i])

print(val)

