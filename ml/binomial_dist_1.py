from scipy.stats import binom

P = 0.8
N = 4
print 1 - binom.cdf(2, N, P)
print binom.cdf(1, N, P)
