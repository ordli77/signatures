import gurobipy as gp
from problem import problem
from utils import find_dim
from utils import is_neg_def
import numpy as np


def optimise(ES, q_0, lambd, k, phi, alpha, N, order,n_step,n_paths,H,sample_size,Sigma):
    A, b, c = problem(ES,order, phi,q_0,alpha,lambd,k,N)
    eigs=np.linalg.eigvals(A)
    print("Eigenvalues {}".format(eigs))
   # print(np.all(eigs <= 0))
    dim_l = find_dim(2,N)
    m = gp.Model("Unconstrained_QP")
    l = m.addMVar(shape=dim_l,lb=-gp.GRB.INFINITY,ub=gp.GRB.INFINITY, name="l")

    obj = l@A@l + l@b 
    m.setObjective(obj,gp.GRB.MAXIMIZE)
    m.optimize()
    if m.status == gp.GRB.OPTIMAL:
       print("Optimal solution:")
       for i in range(dim_l):
           print(f"l[{i}] = {l.X[i]}")
       print("Objective value:", m.ObjVal)
    else:
       print("No optimal solution found")
    
    return l.X