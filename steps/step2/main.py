#!/usr/bin/env python
""" 12 steps to cfd from https://github.com/csrhau/twelve-step-cfd.git """
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import sys
import time

def advection_sim():
    """ 1 dimensional forwards discretized scheme """
    nx = 410      # Number of x steps
    dx = 2.0/(nx-1) # Length of each step (plane is 2 units long)
    nt = 850    #nt is the number of timesteps we want to calculate
    dt = 0.00125  #dt is the amount of time each timestep covers (delta t)
    c = 1.0      #assume wavespeed of c = 1
    u = np.ones(nx)
    u[.5/dx : 1/dx+1]=2  #setting u = 2 between 0.5 and 1 as per our I.C.s
    plt.plot(np.linspace(0, 2, nx), u)
    for t in range(nt):
      print(t)
      un = u.copy()
      for i in range(1, nx):
        u[i] = un[i] - un[i] * dt/dx * (un[i] - un[i-1])
    plt.plot(np.linspace(0, 2, nx), u)
    plt.show()

def main():
    """ Application Entry Point"""
    advection_sim()
    print('done')

if __name__ == '__main__':
    main()
