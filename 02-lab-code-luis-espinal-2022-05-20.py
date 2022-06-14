"""
File: 02-lab-code-luis-espinal-2022-05-20.py
Name: Luis Espinal
Date: 05-22-2022
Purpose: Week 2 Assignment

"""
selection = input("Please specify if you would like to calculate the circumference using the radius or diameter?""\n")
if selection == 'radius':
    value_entered = int(input("Please enter the radius of the circle: "))
    
    if value_entered > 0:
     print(value_entered)
    circumference = 2 * int(3.14159) * value_entered
    print("The circumference of the circle is " +str(circumference) + ".")



elif selection == 'diameter':
    value_entered = input("Please enter the diameter of the circle: ")
    if value_entered > 0:
     circumference = value_entered * int(3.14159)
     print("The circumference of the circle is " +str(circumference) + ".")
   
else: print("You have entered an invalid value!")

