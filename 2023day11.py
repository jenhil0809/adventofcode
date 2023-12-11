with open("2023day11.txt", "r") as file:
    grid = [line.strip() for line in file]
extra = 0
hash_loc = []
for x in range(len(grid)):
    if "#" not in [line[x+extra] for line in grid]:
        for y in range(len(grid)):
            grid[y] = grid[y][:x+extra] + "!" + grid[y][x+extra:]
        extra += 1
extra = 0
for y in range(len(grid)):
    if "#" not in grid[y+extra]:
        grid.insert(y+extra, "".join(["!" for i in range(len(grid[y+extra]))]))
        extra += 1
    else:
        for x in range(len(grid[y+extra])):
            if grid[y+extra][x] == "#":
                hash_loc.append([x, y+extra])
total = 0
for a in range(len(hash_loc)):
    for b in range(len(hash_loc)):
        if a < b:
            total += abs(hash_loc[a][0]-hash_loc[b][0])+abs(hash_loc[a][1]-hash_loc[b][1])
            for i in range(abs(hash_loc[a][0]-hash_loc[b][0])):
                if hash_loc[a][0] > hash_loc[b][0]:
                    if grid[hash_loc[a][1]][hash_loc[a][0]-i] == "!":
                        total += 999998
                else:
                    if grid[hash_loc[b][1]][hash_loc[b][0]-i] == "!":
                        total += 999998
            for i in range(abs(hash_loc[a][1]-hash_loc[b][1])):
                if hash_loc[a][1] > hash_loc[b][1]:
                    if grid[hash_loc[a][1]-i][hash_loc[a][0]] == "!":
                        total += 999998
                else:
                    if grid[hash_loc[b][1]-i][hash_loc[b][0]] == "!":
                        total += 999998
print(total)
