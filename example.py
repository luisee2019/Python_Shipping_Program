"""
Complete the code by replacing the comments with actual Python statements.

Note: The randint() function returns a random integer between its two arguments. So randint(1, 3) returns a random number between 1 and 3, inclusive.

We want to loop and reduce the value of magic_number by some random number each time through the loop. Then we add the current value of magic number to our collected_values list.

If magic_number becomes zero or less, stop the loop.

If magic_number is evenly divisible by 6, immediately cycle the loop from the top, do not add it to the collected_values list.

Replace comment 1 with the statement that will loop until magic_number is less than or equal to zero. For the purposes of this test, you should ignore initial whitespace.
"""

import random
collected_values = []
magic_number = random.randint(0, 10000)
# comment 1 
while magic_number <= 0:
    magic_number = magic_number - random.randint(0, magic_number)
if magic_number % 6 == 0:
            # comment 2
    collected_values.append(magic_number)
print(magic_number)