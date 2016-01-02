from scipy.stats import binom

P = 0.12
N = 10
print round(binom.cdf(2, N, P), 3)
print round(1 - binom.cdf(1, N, P), 3)
