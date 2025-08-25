import gurobipy as gp
from problem import problem
from utils import find_dim
from utils import is_neg_def
import numpy as np


def optimise_qp(ES, q_0, lambd, k, phi, alpha, N, order,n_step,n_paths,H,sample_size,Sigma):
    A, b, c = problem(ES,order, phi,q_0,alpha,lambd,k,N)
    eigs=np.linalg.eigvals(A)
    #A = A*(1e4)#-np.diag(np.ones(15)*(1e-9))
    #b = b*(1e4)
    print("Eigenvalues {}".format(eigs))
   # print(np.all(eigs <= 0))
    dim_l = find_dim(2,N)
    try:
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
           return l.X
        else:
           print("No optimal solution found")
    
        

    except Exception as e:
        print(f"Gurobi failed: {e}")
        return None
