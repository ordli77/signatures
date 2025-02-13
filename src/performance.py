import utils
import numpy as np

def cost(samples,l,q_0,lambd,alpha,phi,k,N,order,n_step,n_paths,H,sample_size,sigma):
    costs=np.array([])
    for path in samples:
        c = utils.Cost(path,utils.sig_speed(l,N),q_0,lambd,alpha,phi,k,N,order)
        costs=np.append(costs,c)
    return costs
