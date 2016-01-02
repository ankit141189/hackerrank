class NormalDistribution(object):
    """Class to represent normal distrbution with the given mean
     and standard deviation"""
    
    def __init__(self, mean=0.0, sigma=1.0):
        self.mean = float(mean)
        self.sigma = float(sigma)

    def ToStdNormalVar(self, x):
        return (x - self.mean) / self.sigma