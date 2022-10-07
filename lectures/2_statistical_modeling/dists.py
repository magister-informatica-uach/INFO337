import scipy.stats
import numpy as np

class GaussianMixture:
    
    def __init__(self, locs, scales, weights):
        self.weights = weights
        self.dists = []        
        for loc, scale in zip(locs, scales):
            self.dists.append(scipy.stats.norm(loc=loc, scale=scale))
            
    def pdf(self, x):
        px = 0.0
        for dist, weight in zip(self.dists, self.weights):
            px += weight*dist.pdf(x)
        return px
    
    def rvs(self, N, seed=None):
        samples = []
        for dist, weight in zip(self.dists, self.weights):
            samples.append(dist.rvs(size=int(weight*N), random_state=seed))
        return np.concatenate(samples)
  