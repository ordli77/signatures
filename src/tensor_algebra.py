import numpy as np
import torch
from esig import tosig

class Tensor():
    
    def __init__(self,dim,order,signature):
    #this dimension should be the maximal dim we need for the extended tensor, which is d
        self.dim = dim
        self.order = order
        array = [[1]]
        
        keys = list(self.sigkeys(2,self.order))
        

        self.value = [torch.zeros([self.dim] * i) for i in range(self.order+1)]
        
        for val, key in zip(signature, keys):
            self[key] = val
            
    def sigkeys(self,dim,order):
        liste=tosig.sigkeys(dim,order).split()
        for i,e in enumerate(liste):
            if isinstance(eval(e),int):
                liste[i] = tuple([eval(e)])
            else:
                liste[i]=eval(e)
        liste = [tuple(np.array(t) - 1) for t in liste]
        return liste
    

    def __getitem__ (self,key):
        
        assert len(key)<= self.order,"length of the key is larger than order of signature %r"%len(key)
        return(self.value[len(key)][key])
    
    def __setitem__(self,key,value):
        
        assert len(key)<= self.order,"length of the key is larger than order of signature %r" % len(key)
        self.value[len(key)][key]=value

    def flatten(self):
        v = []
        for val in self.value:
            v = np.r_[v, val.detach().numpy().flatten()]
        return v
