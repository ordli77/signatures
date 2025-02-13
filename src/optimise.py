import numpy as np
from problem import problem
from utils import find_dim
import cvxpy as cp

def optimise(ES, q_0, lambd, k, phi, alpha, N, order,n_step,n_paths,H,sample_size,sigma):
    A, b, c = problem(ES,order, phi,q_0,alpha,lambd,k,N)
    
    dim_l = find_dim(2,N)
    
    l = cp.Variable(dim_l)
    objective = cp.Maximize(cp.quad_form(l, A) + b * l)
    problems = cp.Problem(objective)
    problems.solve()
    
    return l.value
