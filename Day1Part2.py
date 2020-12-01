input = [] #Creating empty list
with open("C:\\www\\AdventOfCode\\Day1Input") as file: #Import file and format the strings to integers
    for line in file:
        splitted_line = line.split(' ')
        for values in splitted_line:
            value = int(values)
            input.append(value)

Goal = 2020 #Setting our Goal Sum of 3 numbers

def f(input, arr_size, Goal):

    # Set the first number as input[i]
    for i in range( 0, arr_size-2):

        # Set the second number as input[j]
        for j in range(i + 1, arr_size-1):

            # Find the third number that equals the Goal
            for k in range(j + 1, arr_size):
                if input[i] + input[j] + input[k] == Goal:
                    print("Triplet is", input[i], ", ", input[j], ", ", input[k]) #If answer is found print the answer
                    Answer = input[i] * input[j] * input[k] #Take the 3 numbers and multiply them together
                    print(Answer) #Print the product of the 3 numbers
                    return True

    # If we reach this then answer wasn't found
    print("Goal couldn't be found")
    return False

arr_size = len(input)
f(input, arr_size, Goal)
