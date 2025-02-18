import numpy as np
import utils
from optimise import optimise
from process.bm import BM
from process.fbm import FBM
from sample import generate_sample
from plot import plot
import performance
import matplotlib.pyplot as plt





def get_costs(params,Sigma,name):
    
    
    if name =="BM":#generate the midprice process
        process = BM(sigma=Sigma)
    else:
        process = FBM(H=params["H"],sigma=Sigma,n=100)
    
    paths, ES,std,mean= process.build( n_paths=params["n_paths"], order=params["order"])
    #
    ############################################
    #save the price paths into a parameter specified txt file                  
    #try:
    with open("C:\\Users\\gerar\\project1\\data\\midprice of n={},H={} and order{},sigma{}.txt".format(params["n_step"],params["H"],params["order"],Sigma), "w") as txt_file:
        for line in paths:
            txt_file.write("{}".format(params["order"]) + " ".join(map(str, line) )+ "\n")
    #except FileExistsError:
       #print(f&quot;The file "midprice of n={},H={} and order{}.txt".format(params["n_step"],params["H"],params["order"]) already exists.&quot;)
    ############################################
    #run the optimization algorithm, obtain the l as vector of coefficients
    params["sigma"]=Sigma
    l=optimise(ES,**params) 
    with open("C:\\Users\\gerar\\project1\\data\\coeffecient{}.txt".format(Sigma), "w") as f:
    
       f.write(name +"{}".format(l))
    ############################################
     #generate the independent testing samples
                      
    samples = generate_sample(params["sample_size"],params["H"],params["n_step"],params["order"],Sigma,name)
                      
    ############################################
     #evaluate the model using the testing sets, and plot the terminal wealth distribution,the dynamic of the inventory, and trading speeds
    
    speeds, inventories, wealths = utils.get_analytics(utils.sig_speed(l,params["N"]),paths,**params)
 
    #plot(wealths,inventories,speeds)                
    
    
    ##############################################################
    #compute the terminal wealth numerically, and estimate the second stage monte carlo error 

    costs = performance.cost(paths,l,**params)

    mean = np.mean(costs)
    stds = np.std(costs)
    sample_size=params["n_paths"]
    confidence_interval=utils.confidence_interval(mean,sample_size,0.05,stds)

    with open("C:\\Users\\gerar\\project1\\data\\results of steps_test {}, Hurst {},{} and order {}.txt".format(params["n_step"],params["H"],Sigma,params["order"]), "w") as file:
    
       file.write("terminal wealth_test {} Monte carlo error {}".format(mean,np.mean(confidence_interval)))
    return(mean, np.mean(confidence_interval))

