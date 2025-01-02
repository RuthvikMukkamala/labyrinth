

class Graph():

	def __init__(self, graph: dict = {}):
		self.graph = graph


	def printSolution(self, dist):
		print("Vertex \t Distance from Source")


	def add_edge(self, node1, node2, weight):
		if node1 not in self.graph:
			self.graph[node1] = {}
		self.graph[node1][node2] = weight 


def dijstrasAlgorithm(start, end):
	...