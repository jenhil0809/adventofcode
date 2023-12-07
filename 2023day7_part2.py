with open("2023day7.txt", "r") as file:
    lst = [line.split() for line in file]
    hands = [line[0] for line in lst]

five_kind = []
four_kind = []
full_house = []
three_kind = []
two_pair = []
one_pair = []
high_card = []
char_from = "AKQT98765432J"
char_to = "ABCDEFGHIKLMN"
for hand in lst:
    hand[0] = [digit for digit in hand[0]]
    for i in range(5):
        hand[0][i] = char_to[char_from.index(hand[0][i])]
    hand[0] = "".join(hand[0])


def find_hand_type(hand):
    sorted_hand = [card for card in hand]
    sorted_hand.sort()
    if sorted_hand[0] == sorted_hand[1] == sorted_hand[2] == sorted_hand[3] == sorted_hand[4]:
        return 6
    elif (sorted_hand[0] == sorted_hand[1] == sorted_hand[2] == sorted_hand[3] or
          sorted_hand[1] == sorted_hand[2] == sorted_hand[3] == sorted_hand[4]):
        return 5
    elif ((sorted_hand[0] == sorted_hand[1] == sorted_hand[2] and sorted_hand[3] == sorted_hand[4]) or
          (sorted_hand[0] == sorted_hand[1] and sorted_hand[2] == sorted_hand[3] == sorted_hand[4])):
        return 4
    elif (sorted_hand[0] == sorted_hand[1] == sorted_hand[2] or sorted_hand[1] == sorted_hand[2] == sorted_hand[3] or
          sorted_hand[2] == sorted_hand[3] == sorted_hand[4]):
        return 3
    elif (sorted_hand[0] == sorted_hand[1] and sorted_hand[2] == sorted_hand[3] or
          sorted_hand[0] == sorted_hand[1] and sorted_hand[3] == sorted_hand[4] or
          sorted_hand[1] == sorted_hand[2] and sorted_hand[3] == sorted_hand[4]):
        return 2
    elif (sorted_hand[0] == sorted_hand[1] or sorted_hand[1] == sorted_hand[2] or
          sorted_hand[2] == sorted_hand[3] or sorted_hand[3] == sorted_hand[4]):
        return 1
    else:
        return 0


def best_hand(hand):
    cards = "ABCDEFGHIKLM"
    if hand[0].count("N") == 0:
        best = find_hand_type(hand[0])
    if hand[0].count("N") == 1:
        best = (max([find_hand_type(hand[0].replace("N", c, 1)) for c in cards]))
    if hand[0].count("N") <= 1:
        if best == 6:
            five_kind.append(hand)
        elif best == 5:
            four_kind.append(hand)
        elif best == 4:
            full_house.append(hand)
        elif best == 3:
            three_kind.append(hand)
        elif best == 2:
            two_pair.append(hand)
        elif best == 1:
            one_pair.append(hand)
        elif best == 0:
            high_card.append(hand)
    elif hand[0].count("N") == 2:
        best = (max([find_hand_type(hand[0].replace("N", c, 1)) for c in cards]))
        if best == 5:
            five_kind.append(hand)
        elif best == 3:
            four_kind.append(hand)
        elif best == 2:
            full_house.append(hand)
        elif best == 1:
            three_kind.append(hand)
    elif hand[0].count("N") == 3:
        best = (max([find_hand_type(hand[0].replace("N", c, 1)) for c in cards]))
        if best >= 3:
            five_kind.append(hand)
        elif best == 2:
            four_kind.append(hand)

    else:
        five_kind.append(hand)


for hand in lst:
    best_hand(hand)

five_kind.sort(reverse=True)
four_kind.sort(reverse=True)
full_house.sort(reverse=True)
three_kind.sort(reverse=True)
two_pair.sort(reverse=True)
one_pair.sort(reverse=True)
high_card.sort(reverse=True)
total_list = high_card + one_pair + two_pair + three_kind + full_house + four_kind + five_kind
total = 0
for i in range(len(total_list)):
    total += (i + 1) * int(total_list[i][1])
print(total)
