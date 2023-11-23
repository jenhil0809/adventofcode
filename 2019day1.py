lines = []
total = 0
#part 1
with open("day1.txt", "r") as file:
    for line in file:
        lines.append(int(line.strip()))
for val in lines:
    total += val//3-2
print(total)