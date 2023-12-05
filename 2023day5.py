#part 1
with open("2023day5.txt", "r") as file:
    lst = [line.strip() for line in file]

seeds_lst = lst[0][7:].split()

break_lst = ([i for i, x in enumerate(lst) if x == ""])
for i in range(len(break_lst)):
    if i < len(break_lst)-1:
        mapping = lst[break_lst[i]+2:break_lst[i+1]]
    else:
        mapping = lst[break_lst[i]+2:]
    for n in range(len(seeds_lst)):
        found = False
        for x in mapping:
            if int(x.split()[1]) <= int(seeds_lst[n]) < (int(x.split()[1])+int(x.split()[2])) and not found:
                if int(x.split()[0])+(int(seeds_lst[n])-int(x.split()[1])) not in seeds_lst:
                    seeds_lst[n] = int(x.split()[0])+(int(seeds_lst[n])-int(x.split()[1]))
                found = True
print(min(seeds_lst))

#part 2
seeds_lst, *blocks = open("2023day5.txt").read().split("\n\n") #get input split into blocks and keep seeds seperate
seeds_lst = list(map(int, seeds_lst.split(":")[1].split()))

seeds = []

for i in range(0, len(seeds_lst), 2):
    seeds.append((seeds_lst[i], seeds_lst[i] + seeds_lst[i + 1])) #start and end of ranges of seeds

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new = []
    while seeds: #while list not empty
        start_seed, end_seed = seeds.pop() #remove start and end of a range
        for map_start_to, rng_start, rng_len in ranges:
            start_overlap = max(start_seed, rng_start)
            end_overlap = min(end_seed, rng_start + rng_len)
            if start_overlap < end_overlap: #check for overlaps
                new.append((start_overlap - rng_start + map_start_to, end_overlap - rng_start + map_start_to))
                if start_overlap > start_seed:
                    seeds.append((start_seed, start_overlap))
                if end_seed > end_overlap:
                    seeds.append((end_overlap, end_seed))
                break
        else:
            new.append((start_seed, end_seed))
    seeds = new

print(min(seeds)[0])