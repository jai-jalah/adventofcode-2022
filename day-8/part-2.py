'''
Part 1 Steps

# 1. Answer is number of trees visible from outside the grid.
# 2. If tree is on the edge (outermost left, right, top, bottom), then remove it - it will always be visible.
# 3. For each char/number in string, go in each direction.
    # 3a. Is there just one char/number that is larger than the original tree going left, all the way to the edge? If so, this tree is not visible from the left.
    # 3b. If not, it is visible from the left.
    # 3c. Repeat for all directions - if it is visible from at least one direction, then add it to the answer.

Part 2 Steps

# 1. Find how many trees you can go in each direction from a tree, before it is blocked. 
		I.e. 3, 2, 3 - two trees until the first tree's vision is blocked. Find this for each direction.
# 2. Find the scenic score by multiplying the score for each direction.
# 3. What is the highest scenic score possible with the input given?
 
'''

def calculate_horizontal_visibility_counts(tree, tree_row, tree_index):
	left_side_visible = True
	right_side_visible = True
	
	num_of_left_side_trees_visible = 0
	num_of_right_side_trees_visible = 0

	left_trees_list = list()

	for validation_tree_index, validation_tree in enumerate(tree_row):
		if validation_tree_index < tree_index:
			left_trees_list.append(validation_tree)

	left_trees_list.reverse() # We need to check the left nums/trees from inwards to outwards, so we create a new list for left_trees specifically and reverse it.

	for validation_tree_index, validation_tree in enumerate(left_trees_list):
		if left_side_visible:
			if validation_tree < tree:
				num_of_left_side_trees_visible += 1
			else:
				num_of_left_side_trees_visible += 1
				left_side_visible = False
		
	for validation_tree_index, validation_tree in enumerate(tree_row):
		if right_side_visible and validation_tree_index > tree_index:
			if validation_tree < tree:
				num_of_right_side_trees_visible += 1
			else:
				num_of_right_side_trees_visible += 1
				right_side_visible = False

	return num_of_left_side_trees_visible, num_of_right_side_trees_visible
	

def calculate_vertical_visiblity_counts(tree, tree_index, tree_row_index, trees): 
	top_side_visible = True
	bottom_side_visible = True

	num_of_top_side_trees_visible = 0
	num_of_bottom_side_trees_visible = 0

	vertical_trees = list()
	top_trees_list = list()

	for validation_tree_row_index, validation_tree_row in enumerate(trees):
		for validation_tree_index, validation_tree in enumerate(validation_tree_row):
			if validation_tree_index == tree_index:
				vertical_trees.append(validation_tree)

				if validation_tree_row_index < tree_row_index:
					top_trees_list.append(validation_tree)

	top_trees_list.reverse() # We need to check the top nums/trees from inwards to outwards, so we create a new list for top_trees specifically and reverse it.

	for validation_tree_index, validation_tree in enumerate(top_trees_list):
		if top_side_visible:
			if validation_tree < tree:
				num_of_top_side_trees_visible += 1
			else:
				num_of_top_side_trees_visible += 1
				top_side_visible = False
			
	for validation_tree_index, validation_tree in enumerate(vertical_trees):
		if bottom_side_visible and validation_tree_index > tree_row_index:
			if validation_tree < tree:
				num_of_bottom_side_trees_visible += 1
			else:
				num_of_bottom_side_trees_visible += 1
				bottom_side_visible = False
				
	return num_of_top_side_trees_visible, num_of_bottom_side_trees_visible


def calculate_max_scenic_score(trees):
	scenic_scores = list()
	
	for tree_row_index, tree_row in enumerate(trees):
		for tree_index, tree in enumerate(tree_row):
				left_side_visible_count, right_side_visible_count = calculate_horizontal_visibility_counts(tree, tree_row,tree_index)
				top_side_visible_count, bottom_side_visible_count = calculate_vertical_visiblity_counts(tree, tree_index, tree_row_index, trees)
				
				scenic_score = left_side_visible_count * right_side_visible_count * top_side_visible_count * bottom_side_visible_count
				scenic_scores.append(scenic_score)
			
	print(f"Highest Scenic Score possible: {max(scenic_scores)}")
				
	
trees = open("./input.txt").read().splitlines()
calculate_max_scenic_score(trees)
