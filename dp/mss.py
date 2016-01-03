
def mss(l):
	n = len(l)
	max_sum = 0;
	sum = 0
	for i in range(n):
		if sum + l[i] >= 0:
			sum += l[i]
			max_sum = max(max_sum, sum)
		else:
			sum = 0
	return max_sum


if __name__ == '__main__':
	t = int(raw_input())
	for i in range(t):
		n = int(raw_input())
		l = [int(x) for x in raw_input().split()]
		all_positives = [x for x in l if x > 0]
		if not all_positives:
			print '%d %d' % (max(l), max(l))
		else: 
			print '%d %d' % (mss(l), sum(all_positives))
		 
