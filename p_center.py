# https://www.geeksforgeeks.org/greedy-approximate-algorithm-for-k-centers-problem/

import songpa_data
import graph

x = songpa_data.get_x()
y = songpa_data.get_y()

top_dist = 10**9
top_centers = []

# Python3 program for the above approach
def maxindex(dist, n):
	mi = 0
	for i in range(n):
		if (dist[i] > dist[mi]):
			mi = i
	return mi

def selectKcities(node_length, weights, center_count, default_center):
	dist = [0]*node_length
	centers = []

	for i in range(node_length):
		dist[i] = 10**9
		
	# index of city having the maximum distance to it's closest center
	max_index = default_center
	for i in range(center_count):
		centers.append(max_index)
		for j in range(node_length):

			# updating the distance
			# of the cities to their
			# closest centers
			dist[j] = min(dist[j], weights[max_index][j])
			

		# updating the index of the
		# city with the maximum
		# distance to it's closest center
		max_index = maxindex(dist, node_length)

	return dist[max_index], centers
	# graph.draw_p_center(x,y,centers)

# Driver Code
if __name__ == '__main__':
	#weights = songpa_data.get_distance_matrix()
	weights = songpa_data.get_distance_matrix(x,y)


	n = len(weights[0])
	k = 3

	# Function Call
	for i in range(n):
		max, centers = selectKcities(n, weights, k, i)
		print(max, centers)
		if max < top_dist :
			top_dist = max
			top_centers = centers
	
	print("# result")
	print(top_dist, top_centers)

	graph.draw_p_center(x,y,top_centers)

# This code is contributed by mohit kumar 29.
