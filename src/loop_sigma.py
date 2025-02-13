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

sigmas = np.array([0.02,0.03,0.04,0.05,0.06,0.08])

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

for sig in sigmas:
    get_costs(params,sig)