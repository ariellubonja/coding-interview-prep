# Implement a heap in 30m

# TODO deal with tab issue when selecting newline here in sublime

heaped = 1 # 1st element is sorted by default


def heapSort(A):
	buildHeap(A)

	# So far, we have a Heap, but Array is not sorted in the original sense

	# I don't get why we need the rest
	heaped = len(A)
	for i in range(len(A), 1, -1):
		tmp = A[0]
		A[0] = A[len(A)-1]
		A[len(A)-1] = tmp

		heaped -= 1

		maxHeapify(A, 0)

	return A

# TODO what does this do?
def buildHeap(A):
	# TODO I need to keep track of what is sorted and what isn't

	# Go over parents in the tree and heapify
	for i in range(int(len(A) / 2)-1, -1, -1):
		maxHeapify(A, i) # 1st pass correct (i=2)


def mergeHeaps():
	# TODO

	# Compare first two roots
	# TODO What if we have 3 mini-heaps and we need to merge them?
	# Merge first 2, then merge that w/ 3rd (methinks)

	raise NotImplementedError

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
		raise ValueError("Child can only be 'left' or 'right', not", side)

	return ind

# This overcomplicates it
# val = None
# try:
# 	val = A[ind]
# except IndexOutOfRange: # TODO Whatever this is called
# 	pass # This is not a bad state. It's expected
# return ind, val


def insert():
	raise NotImplementedError


def maxHeapify(A, root):
	if len(A) <= 1:
		return
	# heaped = len(A) # At the start, A is unsorted. How to keep track?
	left = getChild(root, 'left')
	right = getChild(root, 'right')

	# If left doesn't exist
	if left >= len(A):
		if right < len(A):
			# Tree should be balanced left-to-right
			raise ValueError("Left child doesn't exist while right child does. This is impossible")

		return

	largest = root
	old_root = A[root]

	if A[left] > A[largest]:
		largest = left

	if right < len(A) and A[right] > A[left]: # Check if right is not out-of-bounds
		if largest == left and A[right] > A[left]:
			largest = right

	# Swap w/ the largest element
	A[root] = A[largest]  # No effect if root is largest

	if largest == left:
		A[left] = old_root
		maxHeapify(A, left)
	elif largest == right:
		A[right] = old_root
		maxHeapify(A, right)

	# heaped = max(left, right) # TODO does this work with None?
	# if heaped < len(A):

	# TODO What is a min_value for python?
	return



if __name__ == '__main__':
	print(heapSort([2,-3,1,-2,5, 10]))