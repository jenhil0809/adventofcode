with open("2023day6.txt", "r") as file:
    lst = [line for line in file]
    times = lst[0].split()[1:]
    distances = lst[1].split()[1:]
ways = 1
for i in range(len(times)):
    count = 0
    for hold_time in range(int(times[i])):
        if hold_time*(int(times[i])-hold_time) > int(distances[i]):
            count += 1
    ways *= count
print(ways)

time = int(lst[0][5:].replace(" ",""))
distance = int(lst[1][9:].replace(" ",""))
min_max = []
hold_time = 0
found = False
while not found:
    hold_time += 1
    if hold_time*(time-hold_time) > distance:
        found = True
        min_max.append(hold_time)
hold_time = time
found = False
while not found:
    hold_time -= 1
    if hold_time*(time-hold_time) > distance:
        found = True
        min_max.append(hold_time)
print(min_max[1]-min_max[0]+1)