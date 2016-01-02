import normal_dist
from scipy.stats import norm
dist = normal_dist.NormalDistribution(20, 2)
print round(norm.cdf(dist.ToStdNormalVar(19.5)), 3)
print round(norm.cdf(dist.ToStdNormalVar(22)) - norm.cdf(dist.ToStdNormalVar(20)), 3)
