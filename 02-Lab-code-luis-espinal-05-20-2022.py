# This program calculates the circumference of a circle
pi = 3.14159
value = input("Please specify if you would like to calculate the circumference using the radius or diameter?""\n")
if value == 'radius':
    circumference = 2 * pi * value
else:
    circumference = value * pi


print("The circumference of the circle is " +str(circumference) + ".")