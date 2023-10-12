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
my_dict = {"name": name, "hair_color" : hair, "eye_color" : eye, \
           "height" : height, "age" : age, "food": food}

#Get values using the key
print(f"{my_dict['name']} is a {my_dict['height']} inches tall student with {my_dict['hair_color']}hair and {my_dict['eye_color']} eyes. They are {my_dict['age']} years old and their favorite food is {my_dict['food']}.")


