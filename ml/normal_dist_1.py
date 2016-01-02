from scipy.stats import norm
import normal_dist
 
dist = normal_dist.NormalDistribution(30, 4)
print round(norm.cdf(dist.ToStdNormalVar(40)), 3)
print round(norm.sf(dist.ToStdNormalVar(21)), 3)
print round(norm.cdf(dist.ToStdNormalVar(35)) - norm.cdf(dist.ToStdNormalVar(30)), 3)
