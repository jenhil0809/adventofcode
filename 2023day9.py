with open("2023day9.txt", "r") as file:
    lst = [line.strip() for line in file]

extra_sum_1 = 0
extra_sum_2 = 0
for line in lst:
    current_line = line.split()
    line_lst = [current_line]
    while current_line != [0 for i in range(len(current_line))]:
        current_line = [int(line_lst[-1][i])-int(line_lst[-1][i-1]) for i in range(1, len(current_line))]
        line_lst.append(current_line)
    #part 1
    extra = 0
    for i in range(len(line_lst)-1, -1, -1):
        extra += int(line_lst[i][-1])
    extra_sum_1 += extra
    #part 2
    extra = 0
    for i in range(len(line_lst)-1, -1, -1):
        extra = int(line_lst[i][0])-extra
    extra_sum_2 += extra

print(extra_sum_1)
print(extra_sum_2)
