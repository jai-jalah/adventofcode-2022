## Rules

# elves legend - A for Rock, B for Paper, C for Scissors.
# player legend - X for Rock, Y for Paper, Z for Scissors.

# Winner with highest score wins.
# Total score is the sum of scores for each round.
# The score for a single round is the score for the shape player selects (1 for Rock, 2 for Paper, and 3 for Scissors), plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

# 1. Create a dictionary for choice legend, and another dictionary for scoring, with a nested dictionary for outcome status scoring.
# 2. Iterate over input
  # 3. Part 1 of player score is just what choice they played - map to dictionary.
  # 4. Part 2 of player score is the outcome - map to dictionary.
  # 5. Sum two scores, store in list.
# 6. At the end, sum all scores for ans to part 1.

elf_choices = {
  "A" : "Rock",
  "B" : "Paper",
  "C" : "Scissors"
}

player_choices = {
  "X" : "Rock",
  "Y" : "Paper",
  "Z" : "Scissors"
}

scoring_rules = {
  "Rock" : 1,
  "Paper" : 2,
  "Scissors" : 3,
  "Outcomes" : {
    "Win" : 6,
    "Draw" : 3,
    "Loss" : 0
  }
}

list_of_scores = []

def calculate_first_choice_score(player_choice):

  player_choice = player_choices[player_choice]
  player_score = scoring_rules[player_choice]
 
  return player_score

def calculate_outcome(elf_choice, player_score):
    elf_choice = elf_choices[elf_choice]
    elf_score = scoring_rules[elf_choice]

    if elf_score == player_score:
      outcome = "Draw"
    elif elf_score == 1 and player_score == 3 or elf_score == 2 and player_score == 1 or elf_score == 3 and player_score == 2: # Ugly hardcoding because I got lost and this finally got me the answer lol
      outcome = "Loss"
    else:
      outcome = "Win"

      
    player_score = player_score + scoring_rules["Outcomes"][outcome]

    list_of_scores.append(player_score)

with open("input.txt", "r") as input_file:
    input = input_file.readlines()

for round in input:
    player_choice = round[2:3]
    elf_choice = round[:1]

    player_score = calculate_first_choice_score(player_choice)
    calculate_outcome(elf_choice, player_score)

   
part_1_ans = sum(list_of_scores)
print(part_1_ans)



