import sys
import heapq

class UniquenessIndex(object):
	
	def __init__(self, l):
		visited = set()
		self.marked_list = [0] * len(l)
		for i in range(len(l)):
			if l[i] not in visited:
				self.marked_list[i] = 1
				visited.add(l[i])
		self.left_most_occurences = self.__LeftMostOccurences(l)

	def CountUnique(self, i, j):
		return sum(self.marked_list[i:j+1])
	
	def Update(self, i):
		next_occurence = self.left_most_occurences[i] 
		if next_occurence is not None:
			self.marked_list[next_occurence] = 1
		self.marked_list[i] = 0

	def __LeftMostOccurences(self, l):
		lookup = {}
		length = len(l)
		result = [None] * length
		for i in range(length - 1, -1, -1):
			try:
				previous = lookup[l[i]]
				result[i] = previous
			except KeyError:
				pass
			lookup[l[i]] = i
		return result

if __name__ == '__main__':
	n_data = int(raw_input())
	data = [int(x) for x in raw_input().split()]
	n_query = int(raw_input())
	query_list = []
	for i in range(0,n_query):
		query = raw_input().split()
		query_list.append((int(query[0]) - 1, int(query[1]) - 1))
	index = UniquenessIndex(data)
	heapq.heapify(query_list)
	l,r = heapq.heappop(query_list)
	for i in range(n_data):
		if i == l:
			count = index.CountUnique(l, r)
			print 'Query (%d, %d): %d' % (l + 1, r + 1, count)
			try:
				l,r = heapq.heappop(query_list)
			except IndexError:
				break
		index.Update(i) 
		
