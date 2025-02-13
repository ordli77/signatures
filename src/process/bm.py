import numpy as np
from .base import midprice

class BM(midprice):
    
    """
    A class used to generate the Brownian Motion

    ...

    Attributes
    ----------
    T : float
        the trading period
    sigma : float
        scaling parameter for the Brownian Motion
    drift : float
    
    n: int
        number of discretization

    Methods
    -------
    _sig(path,order)
        Return the signature of given order for a given path
        
    _generate(self,seed)
        Generate the midprice process
    """
    
    def __init__(self,T=1,sigma=0.02,drift=0,n=100):
        
        self.T =T
        self.sigma = sigma
        self.drift = drift
        self.n = n
        
    def generate(self):
        dt = self.T/self.n
        
        path = np.ones((self.n+1,2))
        path[0,0]=0
        for i in range(1,self.n+1):
            yi = np.random.normal(self.drift,np.sqrt(dt))
            #optimize the code
            path[i,1] = path[i-1,1]+(yi)*self.sigma
            path[i,0] = dt*i
        
        return path