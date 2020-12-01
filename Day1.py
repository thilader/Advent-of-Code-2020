input = [] #Creating empty list
with open("C:\\www\\AdventOfCode\\Day1Input") as file: #Import file and format the strings to integers
    for line in file:
        splitted_line = line.split(' ')
        for values in splitted_line:
            value = int(values)
            input.append(value)

Goal = 2020 #Setting our Goal Sum of 2 numbers

for i, number in enumerate(input[:-1]): #loop through each combination of 2 numbers
    difference = Goal - number #Set this to the Goal minus each number in input
    if difference in input[i+1:]: #Looking to see if each difference is in the input list, if so print the solution
        print("Solution Found: {} and {}".format(number, difference))
        break

Answer = number * difference #Multiple the 2 numbers of the Goal Sum

print(Answer) #Print the product of the 2 numbers
