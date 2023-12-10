with open("2023day10.txt", "r") as file:
    grid = [[c for c in line.strip()] for line in file]

pipe_types = {"|": ["n", "s"],
              "-": ["w", "e"],
              "L": ["n", "e"],
              "J": ["n", "w"],
              "7": ["s", "w"],
              "F": ["s", "e"],
              'S': ["n", "s", "w", "e"]}

directions = {"n": (-1, 0, "s"),
              "s": (1, 0, "n"),
              "w": (0, -1, "e"),
              "e": (0, 1, "w")}

# find starting position
for x in range(len(grid)):
    for y in range(len(grid[x])):
        place = grid[x][y]
        if place == 'S':
            start = (x, y)

encountered_places = dict()  # steps till place reached

search_queue = [(start, 0)]  # list of positions to be checked
while len(search_queue) > 0:
    current, distance = search_queue.pop(0)
    if current in encountered_places:
        continue
    encountered_places[current] = distance
    x, y = current
    available_directions = pipe_types[grid[x][y]]
    for direction in available_directions:
        new_x, new_y, opposite = directions[direction]
        new = (x + new_x, y + new_y)
        if x + new_x < 0 or x + new_x >= len(grid):
            continue
        if y + new_y < 0 or y + new_y >= len(grid[x + new_x]):
            continue
        target = grid[x + new_x][y + new_y]
        if target not in pipe_types:
            continue
        target_directions = pipe_types[target]
        if opposite in target_directions:
            search_queue.append((new, distance + 1))  # add place to search

max_distance = max(encountered_places.values())

print(max_distance)


def get_piece_type(x, y):
    reachable_directions = []
    for direction in directions:
        new_x, new_y, opposite = directions[direction]
        if x + new_x < 0 or x + new_x >= len(grid):
            continue
        if y + new_y < 0 or y + new_y >= len(grid[x + new_x]):
            continue
        if (x + new_x, y + new_y) not in encountered_places:
            continue
        target = grid[x + new_x][y + new_y]
        if target not in pipe_types:
            continue
        target_directions = pipe_types[target]
        if opposite not in target_directions:
            continue
        reachable_directions.append(direction)
    for piece_type in pipe_types:
        if len(reachable_directions) == len(pipe_types[piece_type]):
            if all([direction in pipe_types[piece_type] for direction in reachable_directions]):
                return piece_type
    return None


grid[start[0]][start[1]] = get_piece_type(start[0], start[1])

for x in range(len(grid)):
    norths = 0
    for y in range(len(grid[x])):
        place = grid[x][y]
        if (x, y) in encountered_places:
            pipe_directions = pipe_types[place]
            if "n" in pipe_directions:
                norths += 1
            continue
        if norths % 2 == 0:
            grid[x][y] = "O"
        else:
            grid[x][y] = "I"

inside_count = "\n".join(["".join(line) for line in grid]).count("I")  # find number of "I"s
print(inside_count)
