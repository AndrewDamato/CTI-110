#Andrew D'Amato
#10/05/23
#Introduction to dictionaries

#Get input from user
name = input("Enter your name: ")
hair = input("Enter your hair color: ")
eye = input("Enter your eye color: ")
height = float(input("Enter height as a decimal: "))
age = int(input("Enter your age: "))
food = input("Whats your favorite food? ")

#Create a dictionary
my_dict = {"Name": name, "Hair_Color" : hair, "Eye_Color" : eye, \
           "Height" : height, "Age" : age, "Food": food}

##Get values using the key
print(f" {my_dict['Name']} is a {my_dict['height']} tall student with {mc_dict['hair']} hair and {mc_dict['eye']} eyes. They are {mc_dict['age']} years old and their favorite food is {mc_dict['food'].}")


