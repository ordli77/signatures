import numpy as np
import utils
from optimise import optimise
from process.bm import BM
from process.fbm import FBM
from sample import generate_sample
from plot import plot
import performance
import matplotlib.pyplot as plt





def get_cost(params,Sigma):
    print('Enter the type of process, BM for brownian motion, FBM for fractional Brownian motion')
    
    name =input()
    if name =="BM":#generate the midprice process
        process = BM(sigma=Sigma)
    else:
        process = FBM(H=params["H"],sigma=Sigma,n=100)
    
    paths, ES,std,mean= process.build( n_paths=params["n_paths"], order=params["order"])
    #
    ############################################
    #save the price paths into a parameter specified txt file                  
    #try:
    with open("midprice of n={},H={} and order{}.txt".format(params["n_step"],params["H"],params["order"]), "w") as txt_file:
        for line in paths:
            txt_file.write("{}".format(params["order"]) + " ".join(map(str, line) )+ "\n")
    #except FileExistsError:
       #print(f&quot;The file "midprice of n={},H={} and order{}.txt".format(params["n_step"],params["H"],params["order"]) already exists.&quot;)
    ############################################
    #run the optimization algorithm, obtain the l as vector of coefficients

    l=optimise(ES,**params) 
    with open("coeffecient.txt", "w") as f:
    
       f.write(name +"{}".format(l))
    ############################################
     #generate the independent testing samples
                      
    samples = generate_sample(params["sample_size"],params["H"],params["n_step"],params["order"],Sigma,name)
                      
    ############################################
     #evaluate the model using the testing sets, and plot the terminal wealth distribution,the dynamic of the inventory, and trading speeds
    
    speeds, inventories, wealths = utils.get_analytics(utils.sig_speed(l,params["N"]),samples,**params)
                      
    plot(wealths,inventories,speeds)                
    
    
    ##############################################################

    costs = performance.cost(samples,l,**params)

    mean = np.mean(costs)
  
    size=params["sample_size"]
    confidence_interval=utils.confidence_interval(mean,size,0.05,std)
    print(mean,np.mean(confidence_interval))
    with open("results of steps {}, Hurst {} and order {}.txt".format(params["n_step"],params["H"],params["order"]), "w") as file:
    
       file.write("terminal wealth {} Monte carlo error {}".format(mean,np.mean(confidence_interval)))
    
