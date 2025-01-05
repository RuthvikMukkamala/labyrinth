def checkAdjacent(row, col, matrix, visited)
	if row in range(len(matrix)) and col in range(matrix[row]) and not visited[row][col] and matrix[row][col] > 0: return True
	return False



def checkNegativeValuesInMatrix(matrix):
	for row in matrix:
		for col in row:
			if col < 0:
				return True

	return False



def minimumPassesOfMatrix(matrix):
	"""
	An integer matrix with unequal height and width - return the minimum number of passes 
	required to convert all negative integers in the matrix to positive intergers

	A negative value can become positive if one or more of it's neighbors are positive,
	calculate the minimum number of times that we need to pass through the matrix to make it positive

	Adjacent definition above, below, right, left
	"""

	passCount = 0
	visited = [[False for col in row] for row in matrix]

	while checkNegativeValuesInMatrix(matrix):
		for i in range(len(matrix)):
			for j in range(len(matrix[i])):
				if visited[i][j]:
					continue

				visited[i][j] = True
				checkAdjacentVal = checkAdjacent(i, j, matrix, visited)

				if checkAdjacent:
					matrix[i][j] *= -1

		passCount += 1

	return passCount


