with open("2023day13.txt", "r") as file:
    current_block = []
    grid = []
    for line in file:
        if line == "\n":
            grid.append(current_block)
            current_block = []
        else:
            current_block.append(line.strip())
    grid.append(current_block)


def num_of_diff(line1, line2, diff):
    d = 0
    for a, b in zip(line1, line2):
        if a != b: d += 1
        if d > diff: break
    return d


def find_mirror(patt, diff=0):
    for r in range(len(patt) - 1):
        d = 0
        for i in range(min(r + 1, len(patt) - r - 1)):
            d += num_of_diff(patt[r - i], patt[r + 1 + i], diff)
            if d > diff: break
        else:
            if d == diff:
                return r + 1, 0
    return find_mirror(list(zip(*patt)), diff)[::-1]


total1 = 0
total2 = 0
for pattern in grid:
    r, c = find_mirror(pattern, 0)
    total1 += c + 100 * r
    r, c = find_mirror(pattern, 1)
    total2 += c + 100 * r
print(total1, total2)
