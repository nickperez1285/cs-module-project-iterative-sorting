def linear_search(arr, target):
    # Your code here
    for x in range(0, len(arr)):
        if arr[x] == target:
            return x


    return -1  # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
	low = 0
	high = len(arr) -1

	while low <= high:
		mid = (low + high) // 2 #// floor division

		if arr[mid] == target:
			return mid
		elif arr[mid] < target:
			low = mid + 1
		else:
			high = mid - 1

	return -1  # not found
