import numpy as np
import scipy.integrate


class func:
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma
        
    def norm(self, x):
        return (1/(np.sqrt(2*np.pi*(self.sigma)**2))*np.exp(-((x - self.mu)**2)/(2*(self.sigma)**2)))
    

f = func(1, 1)
g = func(2, 1.414)

def y_pts(pt):
    y_pt = min(f.norm(pt), g.norm(pt))
    return y_pt

overlap = scipy.integrate.quad(y_pts, -np.inf, np.inf)

print(overlap)
