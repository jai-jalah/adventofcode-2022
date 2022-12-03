# 1. Split the string into two. 
# 2. Remove duplicates from each string.
# 3. Map strings over each other - which char shows up in both?  
# 4. get value of char, with a distinction for lowercase or uppercase.
# 5. add priority to answer/total. 

part_1_answer = 0

with open("input.txt", "r") as box_of_rucksacks:
    rucksacks = box_of_rucksacks.readlines()

for rucksack in rucksacks:
    rucksack_first_compartment  = rucksack[:len(rucksack)//2]
    rucksack_second_compartment = rucksack[len(rucksack)//2:] # (NB: This method accommodates for odd numbered strings too, just in case.)
    
    rucksack_first_compartment_sanitised = "".join(set(rucksack_first_compartment)) 
    rucksack_second_compartment_sanitised = "".join(set(rucksack_second_compartment)) # This will not preserve order of string, so may look strange when printed.
    
    duplicate_char = [char for char in rucksack_first_compartment_sanitised if char in rucksack_second_compartment_sanitised][0]
    
    duplicate_char_priority = ord(duplicate_char.lower()) - 96 if (duplicate_char).islower() else ord(duplicate_char.lower()) - 70 # - 96 gets the ord number down to 1 as starting point (i.e. a = 1), - 70 gets it down to 26 (i.e. A = 27)
   
    part_1_answer = part_1_answer + duplicate_char_priority

print(part_1_answer)