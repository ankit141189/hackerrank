import normal_dist
from scipy.stats import norm

def ToPercent(x):
	assert x >= 0 and x <= 1
	return round(x * 100, 2)

dist = normal_dist.NormalDistribution(70, 10)
print ToPercent(norm.sf(dist.ToStdNormalVar(80)))
print ToPercent(norm.sf(dist.ToStdNormalVar(60)))
print ToPercent(norm.cdf(dist.ToStdNormalVar(60)))
