import numpy as np

import utils
from optimise import optimise_cvx
from process.bm import BM
from process.fbm import FBM
from sample import generate_sample
from plot import plot
import performance
import matplotlib.pyplot as plt
from get_cost import get_costs
import matplotlib.pyplot as plt

sigmas = np.array([0.02])#,0.05,0.06,0.07,0.08,0.09])

params = {
    "n_step":100,
    "n_paths":50000,
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
#print(np.version.version)
print('Enter the type of process, BM for brownian motion, FBM for fractional Brownian motion')
name =input()
#QUASI NEWTON method\ relative error 1 percent
print("we are running {} as the midprice path, with Hurst parameter {}, order {}, and {} steps. ".format(name,params["H"],params["order"],params["n_step"]))
result =np.array([])
for sig in sigmas:
    params["Sigma"] = sig
    cost=get_costs(params,name)
    result=np.append(result,cost[0])

plt.plot(sigmas,result)
plt.show()
print(result)
