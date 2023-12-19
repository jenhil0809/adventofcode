from itertools import count

with open("2023day14.txt") as file:
    ls = [line.strip() for line in file]

board = {i + 1j * j: x for i, l in enumerate(ls) for j, x in enumerate(l)}
blocked = {loc for loc, val in board.items() if val == "#"}
rounds = {loc for loc, val in board.items() if val == "O"}


def tilt(rounds, d=1):
    while True:
        free = board.keys() - rounds - blocked
        new_round = {z - d if z - d in free else z for z in rounds}
        if new_round == rounds:
            return new_round
        rounds = new_round


def find_load(rounds):
    return sum(len(ls) - z.real for z in rounds)


def cycle(rounds):
    for d in (1, 1j, -1, -1j):
        rounds = tilt(rounds, d)
    return rounds


print(find_load(tilt(rounds)))

seen = []
for i in count():
    rounds = cycle(rounds)
    if rounds in seen:
        start = seen.index(rounds)
        break
    seen.append(rounds)

print(find_load(seen[(1000000000 - i) % (start - i) + i - 1]))
