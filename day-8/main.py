'''
Part 1 Steps

# 1. Answer is number of trees visible from outside the grid.
# 2. If tree is on the edge (outermost left, right, top, bottom), then remove it - it will always be visible.
# 3. For each char/number in string, go in each direction.
    # 3a. Is there just one char/number that is larger than the original tree going left, all the way to the edge? If so, this tree is not visible from the left.
    # 3b. If not, it is visible from the left.
    # 3c. Repeat for all directions - if it is visible from at least one direction, then add it to the answer.
    
'''
def is_first_or_last_row(tree_row_index, tree_row_len_indexified):
	if tree_row_index == 0 or tree_row_index == tree_row_len_indexified:
		return True


def is_first_or_last_column(tree_index, tree_column_len_indexified):
	if tree_index == 0 or tree_index == tree_column_len_indexified:
		return True


def is_visible_horizontally(tree, tree_row, tree_index):
	left_side_visible = True
	right_side_visible = True

	for validation_tree_index, validation_tree in enumerate(tree_row):
		if left_side_visible and validation_tree_index < tree_index and validation_tree >= tree:
			left_side_visible = False
		elif right_side_visible and validation_tree_index > tree_index and validation_tree >= tree:
			right_side_visible = False

	if left_side_visible or right_side_visible:
		return True


def is_visible_vertically(tree, tree_index, tree_row_index, trees): 
	top_side_visible = True
	bottom_side_visible = True
	vertical_trees = list()

	for tree_row in trees:
		for validation_tree_index, validation_tree in enumerate(tree_row):
			if validation_tree_index == tree_index:
				vertical_trees.append(validation_tree)

	for validation_tree_index, validation_tree in enumerate(vertical_trees):
		if top_side_visible and validation_tree_index < tree_row_index and validation_tree >= tree:
			top_side_visible = False
		elif bottom_side_visible and validation_tree_index > tree_row_index and validation_tree >= tree:
			bottom_side_visible = False

	if top_side_visible or bottom_side_visible:
		return True


def calculate_num_of_visible_trees(trees):
	total_visible_trees = 0
	
	total_trees_on_edges = (len(trees) - 1) * 4
	total_visible_trees += total_trees_on_edges
	
	for tree_row_index, tree_row in enumerate(trees):
		tree_row_len_indexified = len(trees) - 1
		tree_column_len_indexified = len(tree_row) - 1

		if not is_first_or_last_row(tree_row_index, tree_row_len_indexified):
			for tree_index, tree in enumerate(tree_row):
				if not is_first_or_last_column(tree_index, tree_column_len_indexified):
					if is_visible_horizontally(tree, tree_row,tree_index) or is_visible_vertically(tree, tree_index, tree_row_index, trees):
						total_visible_trees += 1
						print(f"Current Visible Trees Count: {total_visible_trees}")

	print(f"Total Visible Trees: {total_visible_trees}")
	

trees = open("./input.txt").read().splitlines()
calculate_num_of_visible_trees(trees)
