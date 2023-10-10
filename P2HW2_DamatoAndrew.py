#Andrew D'Amato
#10/10/2023
#Working with lists

module1 = float(input("Grade for Module 1: "))
module2 = float(input("Grade for Module 2: "))
module3 = float(input("Grade for Module 3: "))
module4 = float(input("Grade for Module 4: "))
module5 = float(input("Grade for Module 5: "))
module6 = float(input("Grade for Module 6: "))

gradelist = []

gradelist.append(module1)
gradelist.append(module2)
gradelist.append(module3)
gradelist.append(module4)
gradelist.append(module5)
gradelist.append(module6)

grademax = max(gradelist)
grademin = min(gradelist)
gradesum = sum(gradelist)
gradeavg = gradesum / len(gradelist)

print("\nResults ")
print("Lowest Grade:", grademin)
print("Highest Grade:", grademax)
print("Sum of Grades:", gradesum)
print("Grade Average:", (f'{gradeavg:.2f}'))
print("---")
