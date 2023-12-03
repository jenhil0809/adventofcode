with open("2023day3.txt", "r") as file:
    lst = [line.strip() for line in file]

symbols = []  # list of all symbols
symbol_locs = set()  # coordinates of all symbols
star_locs = set()
for y, i in enumerate(lst):
    for x, k in enumerate(i):
        if k != "." and not (k.isnumeric()):
            symbols.append(k)
            symbol_locs.add((x, y))
            if k == "*":  # if star
                star_locs.add((x, y))

lst_nums = []  # list of all numbers
number_active = False
width = len(lst[0])
for y, l in enumerate(lst):
    for x, char in enumerate(l):
        if not number_active and not char.isnumeric():  # is not number
            continue
        elif not number_active:  # is new number
            current_num = char
            number_active = True
            x_start = x
        elif not char.isnumeric():  # end of number
            new_num = int(current_num)
            x_end = x - 1
            lst_nums.append((new_num, x_start, x_end, y))
            number_active = False
            current_num = ""
        else:  # continue number
            current_num += char
            if x == width - 1:  # end of line
                new_num = int(current_num)
                x_end = x
                lst_nums.append((new_num, x_start, x_end, y))  # number, x-coord begin, x-coord end, y-coord
                number_active = False
                current_num = ""

count = 0
for num, x_start, x_end, Y in lst_nums:
    border_points = set()
    for y in range(Y - 1, Y + 2):
        for x in range(x_start - 1, x_end + 2):
            border_points.add((x, y))
    intersection = symbol_locs & border_points  # find intersection between sets
    if len(intersection) > 0:
        count += num
print(count)

ratio = 0
for star_x, star_y in star_locs:
    stars = set()
    star_sharing = []
    for x in range(star_x - 1, star_x + 2):
        for y in range(star_y - 1, star_y + 2):
            stars.add((x, y))  # add coords of those surrounding the stars
    for num, x_start, x_end, y in lst_nums:
        if (x_start, y) in stars or (x_end, y) in stars:
            star_sharing.append(num)
    if len(star_sharing) == 2:  # if * borders two
        N1, N2 = star_sharing
        ratio += N1 * N2  # multiply two values
print(ratio)
