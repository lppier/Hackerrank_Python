# Pg 122 Elements of Programming Interviews in Python: 
# Write a program that returns the size of the largest binary subtree that is complete 

# return val is (complete, height, max_sofar)
def isComplete(node):
	if node is None:
		return (True, -1, 0)

	l_complete, l_height, max_so_far = isComplete(node.left)
	r_complete,r_height, max_so_far = isComplete(node.right) 

	# 1st case, either side is not complete, tree starting from this node is not complete
	if not l_complete or not r_complete:
		return (False, 0, max_so_far)

	# 2nd case, both complete, but l_height = -1 
	if l_height == -1 and r_height >= 0:
		return (False, 0, max_so_far)

	max_so_far = max_so_far if max_so_far > max(l_height r_height)+1 else max(l_height, r_height)+1
	return (True, max(l_height, r_height)+1, max_so_far)
