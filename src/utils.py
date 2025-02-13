import numpy as np
import iisignature
from esig import tosig
import scipy.stats as st
#this script offers the functions for computing the keys of the signature, the terminal wealth, and the trading speeds given l
def get_keys(dim,order):
    # dim: dimension of the path
    # order: the truncation level of the signature
    liste=tosig.sigkeys(dim,order).split()
    for i,e in enumerate(liste):
        if isinstance(eval(e),int):
            liste[i] = tuple([eval(e)])
        else:
            liste[i]=eval(e)
    liste = [tuple(np.array(t) - 1) for t in liste]
    return liste

def trading_speed(path,N,l):
    #the l here is the linear operator, which should be implemented as list,like [ 0,1,0,0,2] stands for word 1+ 2*111
    # how to encode the alphabet? do we really need to encode it?????
    if N == 0:
        sig =[1.]
    
    elif N == 1:
        sig =[1.,]
    else:
        sig = [1.]+iisignature.sig(path,N)
    
    return sig.dot(l)

def sig_speed(l, N):
    def f(path):
        
        if N == 0:
            sig = np.array([1.])
        elif N == 1:
            sig = np.array([1., path[-1, 0] - path[0, 0], path[-1, 1] - path[0, 1]])
        else:
            sig = np.r_[1.,iisignature.sig(path, N)]

        

        return sig.dot(l)
    
    return f

def Cost(path,speed,q_0,lambd,alpha,phi,k,N,order,**kwargs):
    # This function calculated the terminal value numerically, given the price process path, and pre calculated speed
    # approximate the integral with lebesgue integral
    WT = 0
    QT = q_0
    penalty = 0
    dt = path[1,0]-path[0,0]
    perman_impact=0
       
    for i in range(len(path)):
        speeds = speed(np.array(path[:i+1]))
        
        temp_impact = lambd*speeds
            
        
        perman_impact += k*speeds*dt #compute the integral numerically
        

        
        price = path[i,1]- temp_impact - perman_impact
        WT += price* speeds*dt
        QT -= speeds*dt
        penalty += phi*(QT**2)*dt
    PT = path[-1,1] - perman_impact
    
    return WT - penalty + QT*(PT-alpha*QT)   
    


def get_analytics(speed, sample, lambd, q_0, alpha, k, **kwargs):

    paths_Qt = []
    paths_wealth = []
    paths_speed = []

    for path in sample:
        WT = 0
        Qt = [0]
        speeds = []
        permanent_impact = 0
        for i in range(len(path) - 1):
            delta_t = path[i+1,0] - path[i, 0]
            speed_t = speed(np.array(path[:i + 1]))
            permanent_impact += k * speed_t * delta_t

            temporary_impact = lambd * speed_t

            WT += (path[i, 1] - permanent_impact - temporary_impact) * speed_t * delta_t
            Qt.append(Qt[-1] + speed_t * delta_t)
            speeds.append(speed_t)
        
        Qt = q_0 - np.array(Qt)
        WT += Qt[-1] * (path[-1, 1] - permanent_impact  - alpha * Qt[-1])
        paths_Qt.append(Qt)
        paths_wealth.append(WT)
        paths_speed.append(speeds)
    return paths_speed, paths_Qt, paths_wealth

    
    
def get_words(dim,order):
    liste=tosig.sigkeys(dim,order).split()
    for i,e in enumerate(liste):
        if isinstance(eval(e),int):
            liste[i] = tuple([eval(e)])
        else:
            liste[i]=eval(e)
    liste = [tuple(np.array(t) - 1) for t in liste]
    return liste
 
def find_dim(d,order):
        if order == 0:
            return 0
        if order == 1:
            return 3
    
        return tosig.sigdim(d, order)
    
def exact(t):
    
    #return the exact signatures to order 3 for brownian motion
    
    return(np.array([1,t,0,1/2*t**2,0,0,1/2*t,1/6*t**3,0,0,1/4*t**2,0,0,1/4*t**2,0]))

def confidence_interval(mean,n,alpha,std):
    
    #calculate the monte carlo error for given sample size and tolerance level
    return (st.norm.ppf(1-alpha)*std)/np.sqrt(n)  

def is_pos_def(x):
    return np.all(np.linalg.eigvals(x) >= 0)


