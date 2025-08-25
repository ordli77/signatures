import numpy as np
import iisignature
from utils import get_words
from utils import find_dim
from shuffle_product import shuffle, concatenation


def problem(Es,order,phi,q_0,alpha,lambd,k,N):
    
    #this order should be the truncated level
    dim = find_dim(2,N)
    
    A = np.zeros((dim,dim))
    b = np.zeros(dim)
    c = 0
    keys = get_words(2,order)
    words = get_words(2,N)
    alphabet =(0,1)
    for w in words:
        w_idx = keys.index(w)
        words_2 = get_words(2,N)
        for v in words_2:
            v_idx = keys.index(v)
            w_shuffle_v = shuffle(w, v)
            w_shuffle_v_1 = [tuple(list(tau) + [0]) for tau in w_shuffle_v]
            w_shuffle_v_1_t = [tau for tau in w_shuffle_v_1 if len(tau)<=order]
            ES_w_shuffle_v_1 = sum(Es[tau] for tau in w_shuffle_v_1_t)

            w1_shuffle_v = shuffle(tuple(list(w) + [0]), v)
            w1_shuffle_v_t = [tau for tau in w1_shuffle_v if len(tau)<=order]
            ES_w1_shuffle_v = sum(Es[tau] for tau in w1_shuffle_v_t)


            w1_shuffle_v1 = shuffle(tuple(list(w) + [0]), tuple(list(v) + [0]))
            w1_shuffle_v1_t = [tau for tau in w1_shuffle_v1 if len(tau)<=order]

            ES_w1_shuffle_v1 = sum(Es[tau] for tau in w1_shuffle_v1_t )

            w1_shuffle_v1_1 = [tuple(list(tau) + [0]) for tau in w1_shuffle_v1]
            w1_shuffle_v1_1_t = [tau for tau in w1_shuffle_v1_1 if len(tau)<=order]
            #print([len(tau) for tau in w1_shuffle_v1_1])
            ES_w1_shuffle_v1_1 = sum(Es[tau] for tau in w1_shuffle_v1_1_t)

            
            A[w_idx, v_idx] = -lambd * ES_w_shuffle_v_1 + (k - alpha) * ES_w1_shuffle_v1 - (phi + k) * ES_w1_shuffle_v1_1

        
        ES_w = Es[w]

        w_shuffle_2 = shuffle(w, (1,))
        w_shuffle_21 = [tuple(list(tau) + [0]) for tau in w_shuffle_2]
        w_shuffle_21_t = [tau for tau in w_shuffle_21 if len(tau)<=order]
        ES_w_shuffle_21 = sum(Es[tau] for tau in w_shuffle_21_t)

        w1_shuffle_2 = shuffle(tuple(list(w) + [0]), (1,))
        w1_shuffle_2_t = [tau for tau in w1_shuffle_2 if len(tau)<=order]
        ES_w1_shuffle_2 = sum(Es[tau] for tau in w1_shuffle_2_t)

        w1 = tuple(list(w) + [0])
        ES_w1 = Es[w1]

        w11 = tuple(list(w1) + [0])
        ES_w11 = Es[w11]

        b[w_idx] = ES_w_shuffle_21 - ES_w1_shuffle_2 + (2 * alpha * q_0 - q_0 * k) * ES_w1 + 2 * phi * ES_w11

    c = q_0 * (Es[(1,)] + 1.) - alpha *(q_0**2)-(q_0 **2) * phi 
        
   
    return A,b,c
