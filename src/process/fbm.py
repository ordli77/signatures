import numpy as np
import fbm

from .base import midprice

class FBM(midprice):
    """
    A class used to generate the fractional Brownian Motion process

    ...

    Attributes
    ----------
    T : int
        an integer for the trading period
    H : float
        Hurst parameter
    sigma : float
        Parameter for scaling the fBM
    n : int
        the number of discretization steps
    drift: float
        Drift of the BM

    Methods
    -------
    generate(self)
        generate a path of fractional Brownian Motion given the parameter, related to _generate method in midprice class.
    

    """
    def __init__(self, T=1., H=0.25, sigma=0.02, n=100, drift=0.):
        self.sigma = sigma
        self.n = n
        self.drift = drift
        self.T = T
        self.H = H
        
    def generate(self):
        f = fbm.FBM(n=self.n, hurst=self.H, length=1, method='daviesharte')
        #path = np.ones((self.n,2))
        #path[:,1] = 1 + self.drift * f.times() + self.sigma * f.fbm()
        #path[:,0] = f.times()
        path = np.c_[f.times(), 1 + self.drift * f.times() + self.sigma * f.fbm()]
        
        return path
    