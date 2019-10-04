#Finds the area of a polygon defined by a list of vertices
#The points must be in order (i.e. run CW or CCW around the polygon)
def shoelace(points):
	n = len(points)
	s1 = 0
	s2 = 0
	for i in range(n-1):
		s1 += points[i][0]*points[i+1][1]
		s2 += points[i+1][0]*points[i][1]

	#If you remove the 'abs' then the area will be negative if the points run clockwise and positive if the run counter-clockwise
	return 0.5 * abs(s1 + points[n-1][0]*points[0][1] - s2 - points[0][0]*points[n-1][1])

def shoelace1Line(points):
	return [0.5 * abs(sum([points[i][0]*points[i+1][1] - points[i+1][0]*points[i][1] for i in range(n-1)]) + points[n-1][0]*points[0][1] - points[0][0]*points[n-1][1]) for n in [len(points)]][0]
