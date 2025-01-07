def checkBounds(matrix, i, j):
	if i in range(len(matrix)) and j in range(len(matrix[i])): return True
	return False


def find_next_cells(matrix, i, j):
	directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
	output = []

	for dx, dy in directions: 
		bounds = checkBounds(matrix, i + dx, j + dy)
		if bounds and matrix[i + dx][j + dy] != -1:
			output.append((i + dx, j + dy))

	return output