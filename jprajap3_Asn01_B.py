"""
    CS1026a 2023
    Assignment 01 Project 01 - Part B
    Jay Prajapati
    251350172
    jprajap3
    08/06/2023
"""


# The variable "x" represents the lower bound and "y" the upper bound.
def main(x, y):
    # Since the upper bound should be included as a value in the range, I will add one to the initial upper bound so
    # that it can be included in the range.
    for number in range(x, y+1):
        # The for loop will execute over and over again until number is greater than 1. A prime number is a number that
        # can only be divisible by 1 and the number itself -- which does not include 1 as a number.
        if number > 1:
            # Since prime numbers start at 2, this 'for loop' will check all the numbers "i" between 2 and the number
            for i in range(2, number):
                # If the value of the remainder of (number/i) is 0 then the loop will break and the number will be printed
                if number % i == 0:
                    break
            else:
                print(number, "is prime")


# Here we ask the user for an input. The user will input an upper bound and a lower bound of the range.
value1 = int(input("Prime numbers starting at: "))
value2 = int(input("Prime numbers ending at: "))

# First we need to check if the start value is greater than the end value
if value1 > value2:
    print("Incorrect Input: {} is greater than {}".format(value1, value2))
    print("The numbers have been automatically switched.")
# If the if statement proves to be True than 'value1' and 'value2' will be returned to the main() function.
# 'value2' is returned as the lower bound "x" and 'value1' is returned as the upper bound "y".
# This way, if 'value1' > 'value2' the values are switched whe returning the values to the main() function.
    main(value2, value1)

# Else if 'value1' == 'value2' (if 'value1' is the same as 'value2' then do the following)
elif value1 == value2:
    print("There are no prime numbers in the range you have entered. ")

# If all other conditions are false, then the main() function will execute.
else:
    # 'value1' will be returned as the lower bound "x" and 'value2' will be returned as the upper bound "y".
    main(value1, value2)

print("END: Project One <01> – Part B")
print("Jay Prajapati jprajap3 251350172")
