import numpy as np
import iisignature
from esig import tosig
import scipy.stats as st
import math
from itertools import product
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
    return listed

def is_neg_def(x):
    return np.all(np.linalg.eigvals(x) <= 0)


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
    return np.linalg.eigvals(x)


def word_dict(n):

    #n: order
    #return: a dictionary which maps each i to a word

    length = int((1-2**n)/(1-2))
    words = get_words(2,n)
    res = {}
    for i in range(length):
        key = str(i)
        res[key]=words[i]
    return res

def is_one_paired(word):
    '''Check if all 1s in the binary tuple are paired.'''
    binary_str = ''.join(map(str, word)) 
    return '101' not in binary_str and binary_str.count('1') % 2 == 0

def is_ones_grouped_evenly(t):
    """
    Returns True if all 1s in the tuple appear in contiguous groups of even length.
    Otherwise, returns False.
    """
    i = 0
    while i < len(t):
        if t[i] == 1:
            group_start = i
            while i < len(t) and t[i] == 1:
                i += 1
            group_length = i - group_start
            if group_length % 2 != 0:
                return False
        else:
            i += 1
    return True

def get_coef(word,t):
    length =len(word)
    
    m = word.count(0)  # Number of times 't' appears
    n = word.count(1)  # Number of times 'B_t' appears
            
    if n % 2 == 1:  # Odd Brownian integrals vanish
            return 0
    else:  
        if not is_ones_grouped_evenly(word):
            return 0
        else:
            n_pair = n//2 #how many pairs e_1 included
            return (t**m * t**n_pair)/(math.factorial(m+n_pair)*2**n_pair)
            
def tensor_prod(vec,n):
    res = np.array([1])
    for i in np.arange(n):
        res= np.kron(res,vec)
    return res
        
def find_p_q(n):
    results = [(n,1)]
    
    q = 1  
    while (2 * q) <= n: 
        if n % (2 * q) == 0:  # Check if n is divisible by 2 * q
            p = n // (2 * q) 
            results.append((p, q))
        q += 1
    
    return results
def exact(n,t):
    ''' generate an array which includes all the exact expected signatures up to level n at time t'''
    words = word_dict(n)
    res = np.array([1])
    length = int((1-2**n)/(1-2))
    for i in range(1,length):
        word = words[str(i)]
        coeff = get_coef(word,t)
        res=np.append(res,coeff)
    return res

def is_between(n, range_tuple):
    low, high = range_tuple
    if n<low:
        return (False,low - n)
    elif n> high:
        return (False, n-high)
    else:
        return True