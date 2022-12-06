'''
Part 1 Steps

# 1. Start at index of 0 / first char, iterate over input in chunks of 4 with index char as starting char i.e. bvwbjplbgvbhsrlpgdmjqwftvncz - bvwb, vwbj, etc.
# 2. If all chars in chunk are uniq, then this is our start-of-packet marker.
# 3. Get position / index + 1 of final char in start-of-packet market in the total string i.e. 
    bvwbjplbgvbhsrlpgdmjqwftvncz - final chunk is vwbj, so answer is 5.

Part 2 steps

# 1. Increase marker length to 14.
'''

datastream = open("input.txt").read()


# Got this algo on Stack Overflow: https://stackoverflow.com/questions/17357370/implementing-an-algorithm-to-determine-if-a-string-has-all-unique-characters
def unique(string):
  unique_chars = set()
  for char in string:
    if char in unique_chars:
      return False
    unique_chars.add(char)
  return True


marker_length = 14  # Make this 4 for part_1_answer, or 14 for part_2_answer.
index = 0

for char in datastream:
  packet = datastream[index:marker_length]

  if unique(packet):
    print(f"Answer: {marker_length}")
    break
  else:
    index += 1
    marker_length += 1
