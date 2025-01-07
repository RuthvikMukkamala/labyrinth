def zeroSumSubarray(nums):
	if 0 in nums:
		return True

	sums = set([0])
	curSum = 0

	for num in nums:
		curSum += num
		if curSum in sums:
			return True
		sums.add(curSum)

	return False
