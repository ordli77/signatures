import numpy as np

import utils
from optimise import optimise
from process.bm import BM
from process.fbm import FBM
from sample import generate_sample
from plot import plot
import performance
import matplotlib.pyplot as plt
from get_cost import get_costs

n_steps = np.array([2**7,2**8,2**9,2**10])

params = {
    "Sigma":0.08,
    "n_paths":20000,
    "N":3,
    "H":0.7,
    "order": 9,
    "q_0": 1.,
    "k":  1e-4,
    "lambd": 1e-3,
    "alpha": 0.1,
    "phi": 0,
    "sample_size" :10000
}
print(np.version.version)
print('Enter the type of process, BM for brownian motion, FBM for fractional Brownian motion')
name =input()


result =np.array([])
for n_step in n_steps:
    params["n_step"]=n_step
    print("we are running {} as the midprice path, with Hurst parameter {}, order {}, and {} steps. ".format(name,params["H"],params["order"],params["n_step"]))
    cost=get_costs(params,name)
    result=np.append(result,cost[0])

print(result)
