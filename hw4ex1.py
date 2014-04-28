# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 22:37:49 2014

@author: jussi24
"""

from hw4classes import *
import matplotlib.pyplot as plt
import numpy as np

air = Substance(complex(1.00058986,0.0000005),0.001275)
ice = Substance(complex(3.1793,0.0026),0.9169)

snow = Mixture(air,ice)

rho_range = np.arange(0.01,0.9,0.01)

max_gar = np.array([np.sqrt(snow.max_gar(rho)) for rho in rho_range])
brugge = np.array([np.sqrt(snow.bruggeman(rho)) for rho in rho_range])

plt.subplot(2,1,1)
plt.plot(rho_range,real(max_gar),label='Maxwell Garnett')
plt.plot(rho_range,real(brugge),label='Bruggeman')
plt.legend(loc=2)
plt.ylabel(r'$\operatorname{Re}(n)$')
plt.subplot(2,1,2)
plt.plot(rho_range,imag(max_gar),rho_range,imag(brugge))
plt.xlabel(r'$\rho \,$ (g/cm$^3$)')
plt.ylabel(r'$\operatorname{Im}(n)$')
plt.suptitle('Refractive index of snowflakes')