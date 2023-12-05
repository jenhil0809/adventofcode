with open("2023day4.txt", "r") as file:
    lst = [line.strip().split(": ")[1].split("|") for line in file]
total = 0
for line in lst:
    points = 0
    for val in line[0].split():
        if val in line[1].split():
            if points == 0:
                points = 1
            else:
                points *= 2
    total += points
print(total)

cards = []
for line in lst: #create list of number of cards won
    new_cards = 0
    for val in line[0].split():
        if val in line[1].split():
            new_cards += 1
    cards.append(new_cards)
times = [1 for i in range(214)] #number of times card is used
for i in range(214): #go through each card
    for n in range(1, cards[i]+1):
        times[i+n] += times[i]
print(sum(times))