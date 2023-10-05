#Andrew D'Amato
#Date
#Formatting floats

#Get float input from user
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
num3 = float(input("Enter a number: "))
num4 = float(input("Enter a number: "))

product = num1 * num2 * num3 * num4
average = (num1 + num2 + num3 + num4)/4

#Display values with f-string
#Display product and average with 0 decimal places
print(f"{product:.0f} {average:.0f}")

#Display the product and average with 3 decimal places
print(f"{product:.3f} {average:.3f}")

