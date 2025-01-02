def mergeOverlappingIntervals(intervals):
    if not intervals:
		return []

	intervals.sort(key=lambda x: x[0])

	output = [intervals[0]]

	for interval in intervals[1:]:
		last_interval = output[-1]

		if interval[0] <= last_interval[1]:
			output[-1] = [output[-1][0], max(interval[1], last_interval[1])]

		else:

			output.append(interval)


	return output