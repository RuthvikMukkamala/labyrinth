def remove_all_type(array, val):
	ptr = array.index(val)
	while ptr != -1:
		array.pop(ptr)
		ptr = array.index(val)

	return array

def majorityElement(array):

	if len(array) == 0:
		return 0
	if len(array) == 1:
		return 1


	highestCount = 0
	highestCountVal = 0
	counter = len(array)

	while counter > 0:
		min_val = min(array)
		min_count = array.count(min_val)

		if min_count > highestCount:
			highestCount = min_count
			highestCountVal = min_val

		array = remove_all_type(array, val)
		counter = len(array)

	return highestCountVal