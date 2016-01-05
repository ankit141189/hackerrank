apple_fruit_file = open('apple-fruit.txt_out')
apple_company_file = open('apple-computers.txt_out')

def read_values(file):
	freq_dist = {}
	for line in file.readlines():
		key_value = line.split()
		key, value = key_value[0], float(key_value[1])
		freq_dist[key] = value
	return freq_dist

fruit_freq_dist = read_values(apple_fruit_file)
company_freq_dist = read_values(apple_company_file)

words = set(fruit_freq_dist.keys() + company_freq_dist.keys())

fruit_words = set()
company_words = set()
for word in words:
	if word in fruit_freq_dist and word in company_freq_dist:
		if company_freq_dist[word] > fruit_freq_dist[word]:
			company_words.add(word)
		else:
			 fruit_words.add(word)
	elif word in fruit_freq_dist:
		fruit_words.add(word)
	else:
		company_words.add(word)

fruit_words_file = open('fruit_words', 'w')
company_words_file = open('company_words', 'w')
fruit_words_file.write(' '.join(fruit_words) + '\n')
company_words_file.write(' '.join(company_words) + '\n')
 
