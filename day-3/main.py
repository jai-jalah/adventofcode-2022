'''
Part 1 steps

1. Split the string into two. 
2. Remove duplicates from each string.
3. Map strings over each other - which char shows up in both?  
4. get value of char, with a distinction for lowercase or uppercase.
5. add priority to answer/total. 
'''

# part_1_answer = 0

# with open("input.txt", "r") as box_of_rucksacks:
#     rucksacks = box_of_rucksacks.readlines()

# for rucksack in rucksacks:
#     rucksack_first_compartment  = rucksack[:len(rucksack)//2]
#     rucksack_second_compartment = rucksack[len(rucksack)//2:] # (NB: This method accommodates for odd numbered strings too, just in case.)
    
#     rucksack_first_compartment_sanitised = "".join(set(rucksack_first_compartment)) 
#     rucksack_second_compartment_sanitised = "".join(set(rucksack_second_compartment)) # Removing duplicate chars in separate rucksacks - this specific methdod will not preserve order of string, so may look strange when printed.
    
#     duplicate_char = [char for char in rucksack_first_compartment_sanitised if char in rucksack_second_compartment_sanitised][0]
    
#     duplicate_char_priority = ord(duplicate_char.lower()) - 96 if (duplicate_char).islower() else ord(duplicate_char.lower()) - 70 # - 96 gets the ord number down to 1 as starting point (i.e. a = 1), - 70 gets it down to 26 (i.e. A = 27)
   
#     part_1_answer = part_1_answer + duplicate_char_priority

# print(f"Part 1 Answer: {part_1_answer}")

'''
Part 2 steps

1. Split all input into groups of three i.e. 300 / 3 = 100 groups.
2. For each group, find the char that appears in each of the members' rucksacks.
3. Calculate priority of said common character.
4. Answer = total of common chars altogether.
'''  
part_2_answer = 0

with open("input.txt", "r") as box_of_rucksacks:
    rucksacks = box_of_rucksacks.readlines()

for rucksack in range(0, len(rucksacks), 3):
    first_rucksack, second_rucksack, third_rucksack = rucksacks[rucksack:rucksack+3] # Partitions the rucksack list into groups of 3 elements.
 
    first_rucksack_sanitised = ''.join(sorted(set(first_rucksack), key=first_rucksack.index)) 
    second_rucksack_sanitised = ''.join(sorted(set(second_rucksack), key=second_rucksack.index)) 
    third_rucksack_sanitised = ''.join(sorted(set(third_rucksack), key=third_rucksack.index)) # Maintaining the order of string this time around, as keep getting a rogue newline char along with the actual duplicate char and cannot be bothered to figure out how to remove it.
    
    duplicate_char = [char for char in first_rucksack_sanitised if char in second_rucksack_sanitised and char in third_rucksack_sanitised][0]
    
    duplicate_char_priority = ord(duplicate_char.lower()) - 96 if (duplicate_char).islower() else ord(duplicate_char.lower()) - 70 # - 96 gets the ord number down to 1 as starting point (i.e. a = 1), - 70 gets it down to 26 (i.e. A = 27)
   
    part_2_answer = part_2_answer + duplicate_char_priority

print(f"Part 2 Answer: {part_2_answer}")