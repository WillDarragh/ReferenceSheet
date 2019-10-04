#Gift Wrapping Algorithm for finding convex hull given a list of points
#Also called Jarvis March
#Points must be a list of points with no 3 points being colinear (i.e. no 3 points lying on a line)
def giftWrap(points):
	#Set current to be the left most point
	current = sorted(points, key=lambda x: x[0])[0]

	#Will contain all points in the hull
	hull = []

	next = None
	while(len(hull) == 0 or next != hull[0]):
		hull.append(current)

		next = points[0]
		for j in range(len(points)):
			#Checks if points[j] is left of the line from current to next
			#If val < 0 then the point is on the left
			val = (points[j][0] - current[0]) * (next[1] - current[1]) - (points[j][1] - current[1]) * (next[0] - current[0])
			#Skips check if current and next are the same point
			if current == next or val < 0:
				next = points[j]
		current = next

	##Uncomment if you want to connect the last point with the 1st point
	#hull.append(hull[0])
	return hull
