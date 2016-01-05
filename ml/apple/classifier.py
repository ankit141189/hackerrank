import re
import sys
company_words = open('company_words').readline().split()
fruit_words = open('fruit_words').readline().split()
print company_words
n = int(raw_input())
for i in range(n):
	company, fruit = 0, 0
	for word in re.findall(r'\b(\w+)\b', raw_input()):
		if word == 'apple' or word.lower() == 'apples':
			fruit = sys.maxint
		if word.lower() in company_words:
			company += 1
		if word.lower() in fruit_words:
			fruit += 1
	output = 'computer-company' if company >= fruit else 'fruit'
	print output
