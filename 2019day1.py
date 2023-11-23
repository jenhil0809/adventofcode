lines = []
total = 0
with open("day1.txt", "r") as file:
    for line in file:
        lines.append(int(line.strip()))
for val in lines:
    total += val//3-2
    fuel_add = val//3-2
    while fuel_add//3-2 > 0:
        total += fuel_add//3-2
        fuel_add = fuel_add//3-2
print(total)
