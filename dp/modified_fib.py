import sys

input = raw_input().split();
a = int(input[0])
b = int(input[1])
n = int(input[2])

for i in range(3, n+1):
	c = b * b + a
	a = b
	b = c
print b
