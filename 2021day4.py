def rotate_card(card):
    rotated_card = []
    for i in range(len(card[0])):
        line = []
        for j in range(len(card[i])):
            line.append(card[j][i])
        rotated_card.append(line)
    return rotated_card


def get_win(list_numbers, card):
    win_index = -1
    win_score = 0
    rotated = rotate_card(card)
    win = False
    for number in list_numbers:
        for idx in range(len(card)):
            if card[idx].count(number):
                card[idx].pop(card[idx].index(number))
                if len(card[idx]) == 0:
                    win = True
                    for i in range(len(card)):
                        win_score += sum(card[i])
                    break
            if rotated[idx].count(number):
                rotated[idx].pop(rotated[idx].index(number))
                if len(rotated[idx]) == 0:
                    win = True
                    for i in range(len(rotated)):
                        win_score += sum(rotated[i])
                    break
        if win:
            win_index = list_numbers.index(number)
            win_number = number
            break
    return win_index, win_number, win_score


def main():
    with open("2021day4.txt") as file:
        list_numbers = []
        bingo_card = []
        min_win_index = max_win_index = 0
        min_win_score = max_win_score = 0
        min_win_number = max_win_number = 0

        list_numbers = list(map(int, file.readline().split(',')))
        min_win_index = len(list_numbers)
        while True:
            bingo_card = []
            file.readline()
            for _ in range(0, 5):
                bingo_card.append(list(map(int, file.readline().split())))
            if len(bingo_card[0]) == 5:
                cur_win_index, cur_win_number, cur_win_score = get_win(
                    list_numbers, bingo_card)
                if cur_win_index < min_win_index:
                    min_win_index, min_win_score, min_win_number = cur_win_index, cur_win_score, cur_win_number
                if cur_win_index > max_win_index:
                    max_win_index, max_win_score, max_win_number = cur_win_index, cur_win_score, cur_win_number
            else:
                break

        print(min_win_number * min_win_score)
        print(max_win_number * max_win_score)


if __name__ == "__main__":
    main()