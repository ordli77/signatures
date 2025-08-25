import numpy as np
import iisignature
import utils
import tensor_algebra as TA

class midprice(object):
    """
    A class used to represent an the midpprice process

    ...

    Attributes
    ----------
    path : ndarray
        an array with size n*d, n d-dimensional midprice paths
    order : int
        truncation level

    Methods
    -------
    _sig(path,order)
        Return the signature of given order for a given path
        
    _generate(self,seed)
        Generate the midprice process
    """
    
    def __init__(self):
        pass
    
    @staticmethod
    def _sig(path,order):
        return np.r_[1.,iisignature.sig(path,order)]
    
    
    def _generate(self,seed):
        np.random.seed(seed)

        return self.generate()
    
    def generate(self):
        
        pass
        
    def build(self,n_paths,order):


        paths = []
        sigs = []
        for seed in np.arange(n_paths):
            path = self._generate(seed)
            sig = self._sig(path,order)
            sigs.append(list(sig))
            paths.append(path)


#print(paths)
        # Compute signatures
       
  
        std = np.std(sigs,axis=0)
        ExpectedSig = TA.Tensor( 2, order,np.mean(sigs, axis=0))
        mean = np.mean(sigs,axis=0)
        return np.array(paths), ExpectedSig,std,mean
    


