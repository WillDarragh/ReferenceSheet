#Returns the path from the start to a given node
def getPath(cameFrom, node, path=[]):
	if cameFrom[node] is not None:
		return getPath(cameFrom, cameFrom[node], [node] + path)
	return [node] + path

#Dijkstra's Algorithm where graph is an adjacency matrix
#Unconnected nodes are marked with a distance of 0
#Can be easily changed to mark with other values in case 0 distances are needed
def dijkstra(graph, start, goal):
	n = len(graph)

	#Distances for each node defaults to infinity
	#Starting node starts at 0
	dist = [float('inf')] * n
	dist[start] = 0

	#Keeps track of where each node came from
	#Used to generate the path
	cameFrom = [None] * n

	#Keeps track of which nodes have been visited
	visited = [False] * n

	#If current = -1 then there are no more visited nodes that can be reached
	current = start
	while(current != -1):
		#You are done!!!
		#Choose what you want to return
		if current == goal:
			return getPath(cameFrom, goal) #Path from start to goal
			#return dist[goal] #Distance from start to goal

		#Checking each neighbor of current node
		for i in range(n):
			#1st check is if current is connected to the ith node
			#Change if using different method to mark unconnected nodes
			if graph[current][i] and not visited[i]:
				tempDist = dist[current] + graph[current][i]
				if tempDist < dist[i]:
					dist[i] = tempDist
					cameFrom[i] = current

		#Marking current node as visited
		visited[current] = True

		#Finding the unvisited node with the smalled distance
		#Returns -1 if nothing is found
		minD = float('inf')
		minIndex = -1
		for i in range(n):
			if not visited[i]:
				if dist[i] < minD:
					minD = dist[i]
					minIndex = i
		current = minIndex

	#If no longer in loop then there is no path from start to goal
	return None
