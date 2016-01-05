import re
import sys

def OrJoiner(l):
	paranthesized = ['(?:' + exp + ')' for exp in l]
	return '|'.join(paranthesized)

def WordBoundary(exp):
	return r'(?:\b(?:' + exp + r')\b)'

def DayOrdinals():
	l = []
	for d in range(1, 32):
		if d % 10 == 1 and not d == 11:
			l.append((d, 'st'))
		elif d % 10 == 2 and not d == 12:
			l.append((d, 'nd'))
		elif d % 10 == 3 and not d == 13:
			l.append((d, 'rd'))
		else:
			l.append((d, 'th'))
	return OrJoiner(['%d(?:%s)?' % (a, b) for (a, b) in l])  		

class DatePattern:
	DAY = WordBoundary(OrJoiner([r'0?[1-9]', r'[12][0-9]', r'3[01]']))
	MONTH_NUM = WordBoundary(OrJoiner([r'0?[1-9]', r'1[12]']))
	YEAR = WordBoundary(OrJoiner([r'\d{2}', r'\d{4}']))
	SEPARATOR = r'[/\.]'
	DD_MM_YYYY = r'(' + DAY + SEPARATOR + MONTH_NUM + SEPARATOR + YEAR + ')'
	MM_DD_YYYY = r'(' + MONTH_NUM + SEPARATOR + DAY + SEPARATOR + YEAR + ')'
	MONTHS = WordBoundary(OrJoiner(['Jan', 'January', 'Feb', 'February', 'Mar', 'March', 'Apr', 'April',
			'May', 'Jun', 'June', 'Jul', 'July', 'Aug', 'August', 'Sep', 'September',
			'Oct', 'October', 'Nov', 'November', 'Dec', 'December']))
	DAYS_ORDINAL = WordBoundary(DayOrdinals())
	FORMAT_1 = r'(' + DAYS_ORDINAL + ' ' + '(?:of )?' + MONTHS + ',? ' + YEAR + ')'
	FORMAT_2 = r'(' + MONTHS + ' ' + DAYS_ORDINAL + ',? ' + YEAR + ')'
	ALL_FORMATS = DD_MM_YYYY + '|' + MM_DD_YYYY + '|' + FORMAT_1 + '|' + FORMAT_2

t = int(raw_input())
for i in range(t):
	text = raw_input()
	matched_dates = len(re.findall(DatePattern.ALL_FORMATS, text))
	matched_a = len(re.findall(r'\b[aA]\b', text))
	matched_an = len(re.findall(r'\b[aA]n\b', text))
	matched_the = len(re.findall(r'\b[Tt]he\b', text))
	print matched_a
	print matched_an
	print matched_the
	print matched_dates
	raw_input()



