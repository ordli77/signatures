import numpy as np
import utils
from qp import optimise_qp
from optimise import optimise_cvx
from process.bm import BM
from process.fbm import FBM
from sample import generate_sample
from plot import plot
import performance
import matplotlib.pyplot as plt





def get_costs(params,name):
    
    
    if name =="BM":#generate the midprice process
        process = BM(sigma=params["Sigma"],n=params["n_step"])
    else:
        process = FBM(H=params["H"],sigma=params["Sigma"],n=params["n_step"])
    
    paths, ES,std,mean= process.build( n_paths=params["n_paths"], order=params["order"])

    ES_f = ES.flatten()
    #print(ES.value)
    plt.plot(*paths[:100].T, "b", alpha=0.1)
    plt.xlabel("Time")
    plt.ylabel("Unaffected price")
    plt.savefig('foo{}.png'.format(params["Sigma"]))  #
    ############################################
    #save the price paths into a parameter specified txt file                  
    #try:
    #with open("C:\\Users\\gerar\\project1\\data\\midprice of n={},H={} a      nd order{},sigma{}.txt".format(params["n_step"],params["H"],params["order"],params["Sigma"]), "w") as txt_file:
        #for line in paths:
            #txt_file.write("{}".format(params["order"]) + " ".join(map(str, line) )+ "\n")
    #except FileExistsError:
       #print(f&quot;The file "midprice of n={},H={} and order{}.txt".format(params["n_step"],params["H"],params["order"]) already exists.&quot;)
    ############################################
    #run the optimization algorithm, obtain the l as vector of coefficients
 
    l=optimise_qp(ES,**params)
    #if l == None:
        #print("Falling back to CVXPY...")
        #l = optimise_cvx(ES,**params)
    #with open("C:\\Users\\gerar\\project1\\data\\coeffecient{}.txt".format(params["Sigma"]), "w") as f:
    
       #f.write(name +"{}".format(l))
    ############################################
     #generate the independent testing samples
                      
    samples = generate_sample(params["sample_size"],params["H"],100,params["order"],params["Sigma"],name)
                      
    ############################################
     #evaluate the model using the testing sets, and plot the terminal wealth distribution,the dynamic of the inventory, and trading speeds
    
    speeds, inventories, wealths = utils.get_analytics(utils.sig_speed(l,params["N"]),paths,**params)
 
    #plot(wealths,inventories,speeds)                
 #   print(np.mean(speeds,axis=0))
    
    ##############################################################
    #compute the terminal wealth numerically, and estimate the second stage monte carlo error 

    costs = performance.cost(samples,l,**params)
    
    mean = np.mean(costs)
    stds = np.std(costs)
    sample_size=params["sample_size"]
    confidence_interval=utils.confidence_interval(mean,sample_size,0.05,stds)

    #with open("C:\\Users\\gerar\\project1\\data\\results of steps_test {}, Hurst {},{} and order {}.txt".format(params["n_step"],params["H"],params["Sigma"],params["order"]), "w") as file:
    
       #file.write("terminal wealth_test {} Monte carlo error {}".format(mean,np.mean(confidence_interval)))
    return(mean, np.mean(confidence_interval))

