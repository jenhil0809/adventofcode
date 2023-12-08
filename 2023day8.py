from math import lcm

with open("2023day8.txt", "r") as file:
    lst = [line.strip() for line in file]
    directions = lst[0]
    codes = {}
    for line in lst[2:]:
        codes[line[:3]] = [line[7:10], line[12:-1]]

# part 1
current = "AAA"
steps = 0
while current != "ZZZ":
    if directions[steps % len(directions)] == "L":
        current = codes[current][0]
    else:
        current = codes[current][1]
    steps += 1
print(steps)

# part 2
current_lst = [code for code in codes if code[-1] == "A"]
steps_lst = []
for i in range(len(current_lst)):
    steps = 0
    while current_lst[i][-1] != "Z":
        current = current_lst[i]
        if directions[steps % len(directions)] == "L":
            current_lst[i] = codes[current][0]
        else:
            current_lst[i] = codes[current][1]
        steps += 1
    steps_lst.append(steps)
print(lcm(*steps_lst))
