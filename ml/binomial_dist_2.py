from scipy.stats import binom

def CalculateParam(successes, failures):
	return successes / (successes + failures)

P = CalculateParam(1.09, 1)
N = 6
print round(1 - binom.cdf(2, N, P), 3)
