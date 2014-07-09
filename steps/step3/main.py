#!/usr/bin/env python
""" 12 steps to cfd from https://github.com/csrhau/twelve-step-cfd.git """
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import itertools


def heat_equation():
    """ Perform the heat/fourier/diffusion equation in 1d """
    plt.ion()
    plt.show()
    nx = 250
    nt = 25000
    dt = 0.0001
    vis = 0.1 # Thermal coefficient (Or viscosity)
    dx = 2.0 / (nx - 1) # 2 arbitrary units long
    # Create initial hat function
    ua = np.ones(nx)
    ua[.5/dx : 1/dx+1]=2  #setting u = 2 between 0.5 and 1 as per our I.C.s
    ub = ua.copy()
    array_switch = itertools.cycle([ua, ub])
    u = array_switch.next()
    for t in range(nt):
        un = u
        u = array_switch.next()
        for i in range(1, nx-1):
            u[i] = un[i] + vis *  dt / dx**2 * (un[i+1] - 2*un[i] + un[i -1])
        plt.pause(0.00001)
        plt.plot(np.linspace(0, 2, nx), u)
        plt.draw()




def main():
    """ Application Entry Point """
    heat_equation()
    print('Done')

if __name__ == '__main__':
    main()
