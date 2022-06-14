"""
File: 02-lab-code-luis-espinal-2022-05-20.py
Name: Luis Espinal
Date: 05-22-2022
Purpose: Week 2 Assignment

"""
value = input("Please specify if you would like to calculate the circumference using the radius or diameter?""\n")
if value == 'radius' and value > 0:
    value = input("Please enter the radius of the circle: ")
    circumference = 2 * int(3.14159) * value
    print("The circumference of the circle is " +str(circumference) + ".")

elif value == 'diameter' and value > 0:
    value = input("Please enter the diameter of the circle: ")
    circumference = value * int(3.14159)
    print("The circumference of the circle is " +str(circumference) + ".")

else: print("You have entered an invalid value!")

