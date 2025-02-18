import numpy as np
from statsmodels.graphics.tukeyplot import results

import utils
from optimise import optimise
from process.bm import BM
from process.fbm import FBM
from sample import generate_sample
from plot import plot
import performance
import matplotlib.pyplot as plt
from get_cost import get_costs

sigmas = np.array([0.08])

params = {
    "n_step":100,
    "n_paths":20000,
    "N":2,
    "H":0.7,
    "order": 7,
    "q_0": 1.,
    "k":  1e-4,
    "lambd": 1e-3,
    "alpha": 0.1,
    "phi": 0,
    "sample_size" :10000
}
print('Enter the type of process, BM for brownian motion, FBM for fractional Brownian motion')
name =input()
    
result =np.array([])
for sig in sigmas:
    cost=get_costs(params,sig,name)
    np.append(result,cost[0])

print(result)
