input = []
with open("C:\\www\\AdventOfCode\\Day1Input") as file:
    for line in file:
        splitted_line = line.split(' ')
        for values in splitted_line:
            value = int(values)
            input.append(value)

Goal = 2020

for i, number in enumerate(input[:-1]):
    complementary = Goal - number
    if complementary in input[i+1:]:
        print("Solution Found: {} and {}".format(number, complementary))
        break

Answer = number * complementary

print(Answer)
