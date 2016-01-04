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

class Color:
  PURPLE = '\033[95m'
  CYAN = '\033[96m'
  DARKCYAN = '\033[36m'
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  END = '\033[0m'

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

text = sys.stdin.read()
matched = [match.span(0) for match in re.finditer(DatePattern.ALL_FORMATS, text)]

s = ''
previous = 0
for (a,b) in matched:
	s += text[previous:a] + Color.RED + text[a:b] + Color.END
	previous = b
s = s + text[previous:]

print s
