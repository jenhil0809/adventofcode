with (open("2023day2.txt", "r") as file):
    lines = [line.strip().split(": ")[1].split() for line in file]
# part 1
count = 0
for i in range(len(lines)):
    valid = True
    for n in range(len(lines[i]) // 2):
        if ((lines[i][2 * n + 1][:3] == "red" and int(lines[i][2 * n]) > 12) or
                (lines[i][2 * n + 1][:5] == "green" and int(lines[i][2 * n]) > 13) or
                (lines[i][2 * n + 1][:4] == "blue" and int(lines[i][2 * n]) > 14)):
            valid = False
    if valid:
        count += i + 1

print(count)
# part 2
count = 0
for i in range(len(lines)):
    r = 0
    b = 0
    g = 0
    for n in range(len(lines[i]) // 2):
        if (lines[i][2 * n + 1][:3] == "red" and int(lines[i][2 * n]) > r):
            r = int(lines[i][2 * n])
        elif (lines[i][2 * n + 1][:5] == "green" and int(lines[i][2 * n]) > g):
            g = int(lines[i][2 * n])
        elif (lines[i][2 * n + 1][:4] == "blue" and int(lines[i][2 * n]) > b):
            b = int(lines[i][2 * n])
    count += r*g*b

print(count)