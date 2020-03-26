from IPython.display import clear_output
# example set up
import numpy as np
# import optimiser codes
import IscaOpt

settings = {\
    'n_dim': 6,\
    'n_obj': 2,\
    'lb': np.zeros(6),\
    'ub': np.ones(6),\
    'ref_vector': [2.5]*2,\
    'method_name': 'HypI',\
    'budget':100,\
    'n_samples':65,\
    'visualise':True,\
    'multisurrogate':False}

# function settings
from deap import benchmarks as BM
fun = BM.dtlz3
args = (2,) # number of objectives as argument

# optimise
res = IscaOpt.Optimiser.EMO(fun, args, settings=settings)
clear_output()
