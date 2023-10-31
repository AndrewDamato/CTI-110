#Andrew D'Amato
#10/31/2023

num_grades = int(input("How many grades will you enter? "))
#Create empty list
grade_list = []

for grade in range(num_grades):
    this_grade = int(input("Enter a grade: "))
    
    while this_grade < 0 or this_grade > 100:
        print("Invalid grade entered.")
        this_grade = int(input("Enter a grade: "))
        
    grade_list.append(this_grade)
    print(f"{this_grade} has been added to the list")

for grade in grade_list:
    print(grade)


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

