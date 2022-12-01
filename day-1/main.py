
# 1. create a loop with a number (i). that number is the array number.
# 2. run loop on lines. If line = " ", then i+1. We are now onto the next array. Store first array in big boy array.
# 3. sum all nested arrays, get biggest boy number.
# 4. part 2 of puzzle, get three largest numbers and sum them.

big_boy_array = [[]]  # Start with one nested array already (or list, whatever 🙄).
array_num = 0

with open("input.txt", "r") as file:
  text = file.readlines()
  
for line in text:
  if line != "\n": 
    big_boy_array[array_num].append(int(line[:- 1])) # Sanitising number at the end here.
  else:
    array_num = array_num + 1
    big_boy_array.append([])

biggest_boy_array = []

for small_baby_array in big_boy_array:
  biggest_boy_array.append(sum(small_baby_array))
  
biggest_boy_array.sort()

part_1_ans = biggest_boy_array[-1]
# print(part_1_ans)

part_2_ans = sum(biggest_boy_array[-3:])
print(part_2_ans)