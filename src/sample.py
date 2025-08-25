from process.bm import BM
from process.fbm import FBM
def generate_sample(sample_size,H,n_step,order,Sigma,name):
    if name == "BM":
        process_s = BM(n=int(n_step),sigma=Sigma)
        samples, ES_s,std_s,mean_s = process_s.build(n_paths=sample_size,order=order)
    else:
        process_s = FBM(H=H,n=int(n_step),sigma=Sigma)
        samples, ES_s,std_s,mean_s = process_s.build(n_paths=sample_size,order=order)
    
    return samples
