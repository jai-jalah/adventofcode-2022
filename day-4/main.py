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
        part_1_answer = part_1_answer + 1 
    elif pair_2_sanitised[0] >= pair_1_sanitised[0] and pair_2_sanitised[1] <= pair_1_sanitised[1]:
        part_1_answer = part_1_answer + 1

print(part_1_answer)