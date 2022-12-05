'''
Part 1 Steps

# 1. Put crate starting points in dictionary, with values in lists.
# 2. Iterate over steps given in input, splitting the string by numbers.
    # 2a. first num is num_crates_to_move, second num is starting_crate, third num is final_crate.
# 3. from the end of the starting_crate list, remove num_crates_to_move and reverse them, and then append to final_crate list.
# 4. At the end, which crate is the final element in each list? This is the answer.

Part 2 Steps

# 1. No more reversing.

Starting arrangments input:

                [B] [L]     [J]    
            [B] [Q] [R]     [D] [T]
            [G] [H] [H] [M] [N] [F]
        [J] [N] [D] [F] [J] [H] [B]
    [Q] [F] [W] [S] [V] [N] [F] [N]
[W] [N] [H] [M] [L] [B] [R] [T] [Q]
[L] [T] [C] [R] [R] [J] [W] [Z] [L]
[S] [J] [S] [T] [T] [M] [D] [B] [H]
 1   2   3   4   5   6   7   8   9 
'''

crate_arrangements = {
    1: ['S', 'L', 'W'],
    2: ['J', 'T', 'N', 'Q'],
    3: ['S', 'C', 'H', 'F', 'J'],
    4: ['T', 'R', 'M', 'W', 'N', 'G', 'B'],
    5: ['T', 'R', 'L', 'S', 'D', 'H', 'Q', 'B'],
    6: ['M', 'J', 'B', 'V', 'F', 'H', 'R', 'L'],
    7: ['D', 'W', 'R', 'N', 'J', 'M'],
    8: ['B', 'Z', 'T', 'F', 'H', 'N', 'D', 'J'],
    9: ['H', 'L', 'Q', 'N', 'B', 'F', 'T']
}

def flatten(l):
    return [item for sublist in l for item in sublist]

rearrangment_steps = open("input.txt").read().splitlines()

for step in rearrangment_steps:
    num_crates_to_move, starting_crate, final_crate = [int(word) for word in str.split(step) if word.isdigit()]

    indexer = len(crate_arrangements[starting_crate]) - num_crates_to_move # Get elements to remove from front of list.
  
    crate_to_append = crate_arrangements[starting_crate][indexer:] # We make a separate crate with the contents we are moving.
    # crate_to_append.reverse() # Turn this off for part_2_answer.
  
    crate_arrangements[final_crate].append(crate_to_append)
    crate_arrangements[final_crate] = flatten(crate_arrangements[final_crate])

    crate_arrangements[starting_crate] = crate_arrangements[starting_crate][:-num_crates_to_move] # Remove crates that have been moved from the memory of starting_crate.

final_crate_values = list(crate_arrangements.values())
answer_list = list()

[answer_list.append(nested_list[-1:]) for nested_list in final_crate_values]

answer = ('').join(flatten(answer_list)) # Flatten one final time and stringify.
print(answer) # Turn off line 50 / crate_to_append.reverse() for part_2_answer.
