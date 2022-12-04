'''
Part 1 steps

# 1. Does either elf's input contain the others? i.e.
    2 - 8 fully contains 3 - 7.
    4 - 6 fully contians 6 - 6.

    if first num in range 2 >= than first num in range 1, and second num in range 1 =< second num in range 1

    or if the reverse is true.
    
# 2. if true, add +1 to fully_contained_count. Answer is the total count at the end.
'''
assignment_pairs = open("input.txt").read().splitlines()

part_1_answer = 0

for assignment_pair in assignment_pairs:
    split_pairs = assignment_pair.split(",")
    pair_1, pair_2 = (pair.split("-") for pair in split_pairs)

    pair_1_sanitised = [eval(num) for num in pair_1]
    pair_2_sanitised = [eval(num) for num in pair_2] # Converting strings to ints.
  
    if pair_1_sanitised[0] >= pair_2_sanitised[0] and pair_1_sanitised[1] <= pair_2_sanitised[1]:
        part_1_answer += 1
    elif pair_2_sanitised[0] >= pair_1_sanitised[0] and pair_2_sanitised[1] <= pair_1_sanitised[1]:
        part_1_answer += 1

print(f"Part 1 Answer: {part_1_answer}")

'''
Part 2 steps

# 1. Find overlap of both pairs as ranges.
'''
assignment_pairs = open("input.txt").read().splitlines()

part_2_answer = 0

for assignment_pair in assignment_pairs:
    split_pairs = assignment_pair.split(",")
    pair_1, pair_2 = (pair.split("-") for pair in split_pairs)

    pair_1_sanitised = [eval(num) for num in pair_1]
    pair_2_sanitised = [eval(num) for num in pair_2] # Converting strings to ints.
  
    range_overlap = range(max(pair_1_sanitised[0], pair_2_sanitised[0]), min(pair_1_sanitised[-1], pair_2_sanitised[-1])+1) # Found this on stack overflow lol https://stackoverflow.com/questions/6821156/how-to-find-range-overlap-in-python
  
    if len(range_overlap): # will be empty list if no overlap.
        part_2_answer += 1

print(f"Part 2 Answer: {part_2_answer}")


