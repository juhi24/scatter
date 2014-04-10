# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 23:12:12 2014

@author: Jussi Tiira
"""

import numpy as np
import matplotlib.pyplot as plt
from pymiecoated import Mie
from operator import add

class ParticleRange:
    def __init__(self,x_min,x_max,m,samples=1000,name=''):
        self.m = m
        self.name = name
        self.x = 2*np.pi*np.logspace(np.log10(x_min),np.log10(x_max),num=samples)
        self.mie = [Mie(x=x,m=m) for x in self.x]
            
    def params(self,funcname):
        return [getattr(p,funcname)() for p in self.mie]
        
    def plot_eff(self):
        f = plt.figure()
        i = 0
        qstr = {'qext':r'$Q_{ext}$',
                'qsca':r'$Q_{sca}$',
                'qabs':r'$Q_{abs}$',
                'qb':r'$Q_b$'}
        for q in ['qext','qsca','qabs','qb']:
            i += 1
            plt.subplot(4,1,i)
            plt.xlabel('Size parameter')
            plt.ylabel(qstr[q])
            plt.loglog(self.x,self.params(q),self.x,np.array(getattr(self,'ray_'+q)()))
        plt.suptitle('scattering efficiencies of '+self.name)
        f.show()
        
    def plot_ratio(self):
        f = plt.figure()
        plt.title('Mie vs. Rayleigh scattering efficiency ratio with ' + self.name)
        plt.ylabel(r'$Q_{Mie}/Q_{Ray}$')
        plt.xlabel('Size parameter')
        plt.loglog(self.x,map(add,self.params('qsca'),-self.ray_qsca()))
        f.show()
        
    def plot_error(self):
        f = plt.figure()
        plt.title('Absolute error (' + self.name + ')')
        plt.xlabel('Size parameter')
        plt.ylabel(r'$(Q_{Mie}-Q_{Ray}/Q_{Mie}*100%$')
        plt.loglog(self.x,np.subtract(self.params('qsca'),self.ray_qsca()))
        f.show()
        
    def ray_qsca(self):
        return np.array([8/3*x**4*np.absolute(self.alpha())**2 for x in self.x])
        
    def ray_qb(self):
        return self.ray_qsca()
        
    def ray_qabs(self):
        return np.array([4*x*self.alpha().imag for x in self.x])
        
    def ray_qext(self):
        return map(add,self.ray_qabs(),self.ray_qsca())
        
    def alpha(self):
        return (self.m**2-1)/(self.m**2+2)
        

mi = complex(1.310990,3.11e-9)
ma = complex(1.57,0.007)

ice_vis = ParticleRange(1e2/3000,1e3/300,mi,name='ice particles, short wavelenght')
ice_rad = ParticleRange(1e2/3e8,1e3/1e6,mi,name='ice particles, long wavelenght')
aer = ParticleRange(10/3e3,5e3/3e2,ma,name='mineral dust / aerosols')

ptypes = [ice_vis,ice_rad,aer]

for ptype in ptypes:
    ptype.plot_eff()
    ptype.plot_ratio()