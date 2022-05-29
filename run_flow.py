"""
Created on Thu Sep 10 12:04:03 2020
@author: rosie
"""

import os, sys
from time import time
from pydfnworks import * 
from numpy import *

DFN = create_dfn()
# General Work Flow
DFN.dfn_gen()
DFN.dfn_flow()
DFN.dfn_trans()


# Entires 0-3, should be zero here. 
#print(b[0:5])

# JDH- now assigne each of those values for aperture
#b[0] = 1*10**-3 
#b[1] = 1*10**-3 
#b[2] = 1*10**-3 
#b[3] = 1*10**-3 
#b[4] = 5*10**-4
#b[5] = 5*10**-4

# convert perm using the cubic law
#perm[0] = b[0]**2/12
#perm[1] = b[1]**2/12
#perm[2] = b[2]**2/12
#perm[3] = b[3]**2/12
#perm[4] = b[4]**2/12
#perm[5] = b[5]**2/12

# determine values of Transmissivity for determinsitc fractures
#mu = 8.9e-4  #dynamic viscosity of water at 20 degrees C, Pa*s
#g = 9.8  #gravity acceleration
#rho = 997  # water density

#T[0] = (b[0]**3 * rho * g) / (12 * mu)
#T[1] = (b[1]**3 * rho * g) / (12 * mu)
#T[2] = (b[2]**3 * rho * g) / (12 * mu)
#T[3] = (b[3]**3 * rho * g) / (12 * mu)
#T[4] = (b[4]**3 * rho * g) / (12 * mu)
#T[5] = (b[5]**3 * rho * g) / (12 * mu)

#DFN.dump_hydraulic_values(b,perm,T)

# Add transmissivity values to the mesh for visualization
#DFN.add_variable_to_mesh("trans,", "transmissivity.dat", "full_mesh.inp")

## JDH I added an exit here for you to look at the files before you run the simulation.
#exit()

#dfnFlow
#DFN.dfn_flow()


#dfntrans
#DFN.dfn_trans()
