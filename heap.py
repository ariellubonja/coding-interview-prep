# Implement a heap in 30m

# TODO deal with tab issue when selecting newline here in sublime

heap_size = 1 # 1st element is sorted by default

# TODO what does this do?
def heapify(A):
	# TODO I need to keep track of what is sorted and what isn't

	return maxHeapify(A, 0)


def mergeHeaps():
	# TODO

	# Compare first two roots
	# TODO What if we have 3 mini-heaps and we need to merge them?
	# Merge first 2, then merge that w/ 3rd (methinks)



	pass


# [6, 4, 5,2,3,1, 0, -3, 1, 1]
# left = 2*i + 1
# right = 2*i + 2
# index(4) = 1
# => left = 2. A[2]=5 XXX
def getChild(i, side='left'):
	if side == 'left':
		ind = 2 * i + 1
	elif side == 'right':
		ind = 2*i + 2
	else:
		throw IllegalStateException # TODO look this up

	return ind

# This overcomplicates it
# val = None
# try:
# 	val = A[ind]
# except IndexOutOfRange: # TODO Whatever this is called
# 	pass # This is not a bad state. It's expected
# return ind, val


def insert():
	pass


def maxHeapify(A, root):
	if len(A) <= 1:
		return
	# heaped = len(A) # At the start, A is unsorted
	left = getChild(root, 'left')
	right = getChild(root, 'right')
	# root = A[i_root]

	if left >= len(A): # If left doesn't exist
		if right < len(A):
			# Tree should be balanced left-to-right
			raise ValueError("Left child doesn't exist while right child does. This is impossible")

		# Tree is heaped so far, return
		# Ya I don't think that's right.
		# TODO I don't know how to maintain HeapSize state
		# heap_size = max(heap_size, index)
		return

	largest = root

	if A[left] > A[largest]:
		if right < len(A) and A[right] > A[left]: # Check if right is not out-of-bounds
			largest = right
		else:
			largest = left
		old_root = A[root]

		A[root] = A[largest] # Swap w/ the largest element

		if largest == left:
			A[left] = old_root
			maxHeapify(A, left)
		elif largest == right:
			A[right] = old_root
			maxHeapify(A, right)


		  # equivalent to elif len(A) == 2:
		# TODO What is a min_value for python?

	return
	# # if len(A) > 3: # This is not the minimum tree
	# # 	a = maxHeapify(A, 3)
	# # 	A[3:] = a
	# # TODO deal with joining these
	#
	#
	#
	#
	# right = A[2]
	#
	# largest = root
	#
	# if left > largest: # Left child is bigger
	# 	largest = left
	#
	# if right > largest: # Right child is bigger
	# 	largest = right
	#
	# # Swap elements
	# if largest != root: # if root is definitely not the largest element
	# 	if left >= right: # Default to left child if equal
	# 		largest = left # Left is the largest element
	# 		root = largest
	# 		left = root # Move root down left
	# 	else:
	# 		largest = right
	# 		right = root
	# 		root = largest
	#
	# # TODO is this pointer-based?
	# # I think primitives are passed by value in Python. Yes, they need changing
	# A[0] = root
	# A[1] = left
	# A[2] = right
	#
	# return A



if __name__ == '__main__':
	print(heapify([2,-3,1,-2,5, 10]))