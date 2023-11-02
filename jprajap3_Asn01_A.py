"""
CS1026A 2023
Assignment 01 Project 01 - Part A
Jay Prajapati
251350172
jprajap3
2023-09-21
"""

# Since the first two values of the fibonacci sequence are hard coded, we need to set the values ourselves. That is the
# reason why I set the value of variable 'first_number' and 'second_number' to 0.
first_number = 0
second_number = 1

while True:
    # 'sequences' is a variable that will hold a number value. This value will represent the number of repetitions the
    # code will need to make in order to obtain the correct fibonacci sequence.
    sequences = int(input("Sequence ends at: "))
    if sequences < 0:
        print("Please input a positive sequence number. ")
        continue
    elif sequences == 0:
        print("0:", first_number)
    elif sequences == 1:
        # If the user inputs a 'sequence' value of 1, this "hard code" will output only up to sequence 1.
        print("0:", first_number)
        print("1:", second_number)
    else:
        print("0: {} {}".format(first_number, first_number))
        for sequence_number in range(1, sequences + 1):
            # Since at the end of this for loop 'second_number' = 'current_number', this print statement always prints the
            # current numbers in the fibonacci sequence.
            print("{}:".format(sequence_number), second_number, "{:,}".format(second_number))
            # This variable 'current_number' is responsible for holding the value of the sum of the last 2 numbers
            current_number = first_number + second_number
            first_number = second_number
            second_number = current_number
    break

print("END: Project One <01> – Part A")
print("Jay Prajapati jprajap3 251350172")
