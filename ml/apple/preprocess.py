import sys
import math
import re

stopwords_file = open('../stop-word-list.txt')
stopwords = set([x.rstrip() for x in stopwords_file.read().split('\n')])

input_file = open(sys.argv[1])
text = input_file.read().split('\n')
words = []
for line in text:
	for word in re.findall(r'(\b\w+\b)', line):
		if word.lower() not in stopwords and not re.match(r'^\d+$', word):
			words.append(word)

log_total = math.log(len(words))
freq_dist = {}
for w in words:
	try:
		freq_dist[w] = freq_dist[w] + 1
	except KeyError:
		freq_dist[w] = 1

output_file = open(sys.argv[1] + '_out', 'w')

for w, count in freq_dist.iteritems():
	normalized = math.log(count) - log_total
	output_file.write('%s %f\n' % (w.lower(), round(normalized, 5)))

