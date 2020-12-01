input = []
with open("C:\\Users\\adrury\\Downloads\\AdventOfCode\\Day1Input") as file:
    for line in file:
        splitted_line = line.split(' ')
        for values in splitted_line:
            value = int(values)
            input.append(value)

Goal = 2020

def f(input, arr_size, Goal):

    # Fix the first element as A[i]
    for i in range( 0, arr_size-2):

        # Fix the second element as A[j]
        for j in range(i + 1, arr_size-1):

            # Now look for the third number
            for k in range(j + 1, arr_size):
                if input[i] + input[j] + input[k] == Goal:
                    print("Triplet is", input[i], ", ", input[j], ", ", input[k])
                    Answer = input[i] * input[j] * input[k]
                    print(Answer)
                    return True

    # If we reach here, then no
    # triplet was found
    return False

arr_size = len(input)
f(input, arr_size, Goal)
