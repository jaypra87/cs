# Initialize the first two Fibonacci numbers
first_number = 0
second_number = 1

while True:
    sequences = int(input("Sequence ends at: "))
    if sequences < 0:
        print("Please input a non-negative sequence number. ")
        continue
    elif sequences == 0:
        print("0:", first_number)
        break
    else:
        print("0:", first_number)
        for sequence_number in range(1, sequences + 1):
            print("{}:".format(sequence_number), second_number)
            current_number = first_number + second_number
            first_number = second_number
            second_number = current_number
        break
