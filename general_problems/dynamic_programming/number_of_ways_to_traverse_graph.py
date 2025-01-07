
def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.

    ways = [[1 for _ in range(width)] for _ in range(height)]

    for y in range(1, height):
        for x in range(1, width):
            ways[y][x] = ways[y - 1][x] + ways[y][x - 1]

    return ways[-1][-1]
