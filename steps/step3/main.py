#!/usr/bin/env python
""" 12 steps to cfd from https://github.com/csrhau/twelve-step-cfd.git """
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import sys
import time

def linear_conv(nx):
    dx = 2./(nx-1)
    nt = 20    #nt is the number of timesteps we want to calculate
    c = 1
    sigma = .5
    
    dt = sigma*dx

    u = np.ones(nx) 
    u[.5/dx : 1/dx+1]=2

    un = np.ones(nx)

    for n in range(nt):  #iterate through time
        un = u.copy() ##copy the existing values of u into un
        for i in range(1,nx):
            u[i] = un[i]-c*dt/dx*(un[i]-un[i-1])
    plt.plot(np.linspace(0,2,nx),u)
    plt.show()

def main():
    """ Application Entry Point"""
    linear_conv(500)
    print('done')

if __name__ == '__main__':
    main()
