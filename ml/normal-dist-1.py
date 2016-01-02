from scipy.stats import norm
    
class NormalDistribution(object):
    """Class to represent normal distrbution with the given mean
     and standard deviation"""
    
    def __init__(self, mean=0.0, sigma=1.0):
        self.mean = float(mean)
        self.sigma = float(sigma)

    def ToStdNormalVar(self, x):
        return (x - self.mean) / self.sigma
        
normalDist = NormalDistribution(30, 4)
print round(norm.cdf(normalDist.ToStdNormalVar(40)), 3)
print round(norm.sf(normalDist.ToStdNormalVar(21)), 3)
print round(norm.cdf(normalDist.ToStdNormalVar(35)) - norm.cdf(normalDist.ToStdNormalVar(30)), 3)
