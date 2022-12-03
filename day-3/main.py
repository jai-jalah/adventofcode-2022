part_1_answer = 0

with open("input.txt", "r") as box_of_rucksacks:
    rucksacks = box_of_rucksacks.readlines()

for rucksack in rucksacks:
  # 1. Split the string into two. (This method accommodates for odd numbered strings too, just in case.)
    first_half  = rucksack[:len(rucksack)//2]
    second_half = rucksack[len(rucksack)//2:]
    
  # 2. Remove duplicates from each string.
  # This will not preserve order of string, so may look strange when printed.
    first_half = "".join(set(first_half)) 
    second_half = "".join(set(second_half))
    
  # 3. Map strings over each other - which char shows up in both?  
    duplicate_char = [char for char in first_half if char in second_half][0]
    
  # 4. get value of char, with a distinction for lowercase or uppercase.
    duplicate_char_priority = ord(duplicate_char.lower()) - 96 if (duplicate_char).islower() else ord(duplicate_char.lower()) - 70
    # - 96 gets the ord number down to 1 as starting point (i.e. a = 1), - 70 gets it down to 26 (i.e. A = 27)
  
  # 5. add priority to answer/total.  
    part_1_answer = part_1_answer + duplicate_char_priority

print(part_1_answer)



