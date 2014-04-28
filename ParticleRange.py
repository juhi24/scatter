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
    def __init__(self,x_min,x_max,m,samples=1000,name='',wavelength=None):
        self.m = m
        self.name = name
        self.wavelength = wavelength
        self.use_size = wavelength is not None
        if self.use_size:
            x_min = x_min/wavelength
            x_max = x_max/wavelength
            name += ', lambda = ' + str(wavelength)
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
            plt.xlabel(self.xlabel())
            plt.ylabel(qstr[q])
            plt.loglog(self.xvalues(),self.params(q),self.x,np.array(getattr(self,'ray_'+q)()))
        plt.suptitle('scattering efficiencies of '+self.name)
        f.show()
        
    def plot_ratio(self):
        f = plt.figure()
        plt.title('Mie vs. Rayleigh scattering efficiency ratio with ' + self.name)
        plt.ylabel(r'$Q_{Mie}/Q_{Ray}$')
        plt.xlabel(self.xlabel())
        plt.loglog(self.xvalues(),map(add,self.params('qsca'),-self.ray_qsca()))
        f.show()
        
    def plot_error(self):
        f = plt.figure()
        plt.title('Absolute error (' + self.name + ')')
        plt.xlabel(self.xlabel())
        plt.ylabel(r'$(Q_{Mie}-Q_{Ray})/Q_{Mie}*100%$')
        y = 100*np.divide(np.subtract(self.params('qsca'),self.ray_qsca()),self.params('qsca'))
        plt.semilogx(self.xvalues(),y)
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
        
    def part_size(self):
        return self.x*self.wavelength/(2*np.pi)
        
    def xlabel(self):
        if self.use_size:
            return 'Particle size (nm)'
        return 'Size parameter'
        
    def xvalues(self):
        if self.use_size:
            return self.part_size()
        return self.x