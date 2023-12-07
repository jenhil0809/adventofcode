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
char_from = "AKQJT98765432"
char_to = "ABCDEFGHIJKLM"
for hand in lst:
    hand[0] = [digit for digit in hand[0]]
    for i in range(5):
        hand[0][i] = char_to[char_from.index(hand[0][i])]
    hand[0] = "".join(hand[0])


def find_hand(hand):
    sorted_hand = [card for card in hand[0]]
    sorted_hand.sort()
    if sorted_hand[0] == sorted_hand[1] == sorted_hand[2] == sorted_hand[3] == sorted_hand[4]:
        five_kind.append(hand)
    elif (sorted_hand[0] == sorted_hand[1] == sorted_hand[2] == sorted_hand[3] or
          sorted_hand[1] == sorted_hand[2] == sorted_hand[3] == sorted_hand[4]):
        four_kind.append(hand)
    elif ((sorted_hand[0] == sorted_hand[1] == sorted_hand[2] and sorted_hand[3] == sorted_hand[4]) or
          (sorted_hand[0] == sorted_hand[1] and sorted_hand[2] == sorted_hand[3] == sorted_hand[4])):
        full_house.append(hand)
    elif (sorted_hand[0] == sorted_hand[1] == sorted_hand[2] or sorted_hand[1] == sorted_hand[2] == sorted_hand[3] or
          sorted_hand[2] == sorted_hand[3] == sorted_hand[4]):
        three_kind.append(hand)
    elif (sorted_hand[0] == sorted_hand[1] and sorted_hand[2] == sorted_hand[3] or
          sorted_hand[0] == sorted_hand[1] and sorted_hand[3] == sorted_hand[4] or
          sorted_hand[1] == sorted_hand[2] and sorted_hand[3] == sorted_hand[4]):
        two_pair.append(hand)
    elif (sorted_hand[0] == sorted_hand[1] or sorted_hand[1] == sorted_hand[2] or
          sorted_hand[2] == sorted_hand[3] or sorted_hand[3] == sorted_hand[4]):
        one_pair.append(hand)
    else:
        high_card.append(hand)


for hand in lst:
    find_hand(hand)

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
