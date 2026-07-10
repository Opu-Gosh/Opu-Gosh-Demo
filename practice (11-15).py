#problem no. 11
num1 = float(input("Dividend:"))
num2 = float(input("Divisor:"))
Quotient = num1/num2
print(Quotient)

#sortcut
print("The quotient is:", float(input("Dividend:")) / float(input("Divisor:")))
#practice.
distance = float(input("Your distance:"))
time = float(input("Your time:"))
speed = distance/time
print(speed)

#problem no. 12
num3 = float(input("Dividend:"))
num4 = float(input("Divisor:"))
remainder = num3 % num4
print("The remainder is:",remainder)

#problem no. 13
num5 = float(input("The first number:"))
num6 = float(input("The second number:"))
Average = ((num5+num6)/2)
print("The Average value:",Average)

#problem no. 14
num7 = float(input("The first number:"))
num8 = float(input("The second number:"))
num9 = float(input("The third number:"))
Average = ((num7+num8+num9)/3)
print("The Average value:",Average)

#sortcut
nums = [float(input("first num:")),float(input("second num:")),float(input("third num:"))]
average = sum(nums)/len(nums)
print("The average value:",average)

#problem no.15: swapping two variables using a temporary variable.
num9 = int(input("your first number:"))
num10 = int(input("your second number:"))
temp = num9
num9 = num10
num10 = num9
print("swapping : num9:", num9,"num10:",num10)
