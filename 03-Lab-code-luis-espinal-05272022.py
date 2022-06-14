"""
File:  03-Lab-code-luis-espinal-05272022.py
Name: Luis Espinal
Date: 05-27-2022
Purpose: Week 3 Assignment

"""

"""
In this exercise, perform the following steps to keep track of students on a school bus. After each step print the entire list of students 
plus any additional outputs related to the particular step (where applicable). Throughout the following steps, remember that the “bus” 
is representative of a Python list. Only one bus should be used throughout this lab. When a student is referred to by name, you need to 
use the string of that name when operating on the list. When a student is referred to by row or position, you need to use an index value.

    Completed 1.	The bus begins with Dante, Evelyn, Marc, and Grace, each in their own row
    Completed 2.	At stop 1, remove the student in the last row of the bus
    Completed 3.	At stop 2, Chris and Tamara get on the bus, and each sit in their own row at the back of the bus (see if you can do this step with a single command)
    Completed 4.	At stop 3, the bus driver reminds Marc by name to get off at this stop
    Completed 5.	At stop 4, the student in the first row gets off the bus
    Completed 6.	At stop 5, the bus driver rearranges the students to sit from the front of the bus to the back of the bus in reverse alphabetical order
    Completed 7.	At stop 6, the bus driver counts the number of students on the bus, and tells the students how many students are on the bus
    Completed 8.	At stop 7, Goofus and Gallant get on the bus and sit together in the same row at the back of the bus (try using a nested list here)
    9.	At stop 8, the bus driver decides to announce which students are still on the bus, and what order they are in on the bus from front to back
"""
school_bus = ['Dante', 'Evelyn', 'Marc', 'Grace']
print("The school bus begins with the following students" +str(school_bus))

#Stop 1
del school_bus[3]
print("At bus stop number 1 the last student is removed. This leaves the following students on the bus " + str(school_bus))

#Stop 2
school_bus.append('Chris')
school_bus.append('Tamara')
print("At the second bus stop two additinal students get on the bus.  The students on the school_bus are now " +str(school_bus))

#Stop 3
school_bus.remove("Marc")
print("At the third bus stop Marc gets off the bus. The students on the school_bus are now " +str(school_bus))

#Stop 4
del school_bus[0]
print("At the fourth bus stop the student in the first row gets off the bus. The students on the school_bus are now " +str(school_bus))

#Stop 5
school_bus.sort(reverse=True)
print("At the fifth bus stop the students are rearranged to sit from the front of the bus to the back of the bus in reverse alphabetical order. Their seat positions now are as follows " +str(school_bus))

#Stop 6
print("The number of students on the school bus is: "+str(len(school_bus)))

#Stop 7
school_bus = [school_bus, 'Goofus', 'Gallant']
print(school_bus)

#Stop 8
print("The students left on the bus are " + str(school_bus))