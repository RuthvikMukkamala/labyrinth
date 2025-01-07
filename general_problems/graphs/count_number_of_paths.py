def checkBounds(matrix, i, j):
	if i in range(len(matrix)) and j in range(len(matrix[i])): return True
	return False

def count_number_of_paths(matrix, i, j):
	rows, cols = len(matrix), len(matrix[0])
	visited = [[False for _ in range(cols)] for _ in range(rows)]

	for row in rows:
		for col in cols:
			if visited[row][col]:
				continue
			visited[row][col] = True
			dfs(matrix, i, j, visited)

	return sum(sum(row) for row in visited)

def dfs(matrix, i, j, visited):
	directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

	for dx, dy in directions:
		checkBound = checkBounds(matrix, i + dx, j + dy)

		if checkBound:
			visited[i + dx][j + dy] = True
			dfs(matrix, i + dx, j + dy, visited)


