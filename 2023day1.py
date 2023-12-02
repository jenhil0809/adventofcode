def convert(line):
    line = line.replace("one", "one1one")
    line = line.replace("two", "two2two")
    line = line.replace("three", "three3three")
    line = line.replace("four", "four4four")
    line = line.replace("five", "five5five")
    line = line.replace("six", "six6six")
    line = line.replace("seven", "seven7seven")
    line = line.replace("eight", "eight8eight")
    line = line.replace("nine", "nine9nine")
    return line

with (open("2023day1.txt", "r") as file):
    lines = [line.strip() for line in file]

result = [int([char for char in convert(line) if char.isdigit()][0]) * 10
          + int([char for char in convert(line) if char.isdigit()][-1])
          for line in lines]

print(sum(result))
