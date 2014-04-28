# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 14:27:36 2014

@author: jussitii
"""

class Substance:
    def __init__(self,eps,rho):
        self.eps = eps
        self.rho = rho

class Mixture:
    def __init__(self,medium,inclusion):
        self.m = medium
        self.i = inclusion
        
    def fraction(self,rho):
        return (rho - self.m.rho)/(self.i.rho - self.m.rho)
        
    def max_gar(self,rho):
        f = self.fraction(rho)
        eps_diff = self.i.eps - self.m.eps
        return self.m.eps + \
            3*f*self.m.eps*(eps_diff)/(self.i.eps+2*self.m.eps-f*(eps_diff))

    def bruggeman(self,rho):
        f = self.fraction(rho)
        return self.m.eps/2 \
            -self.i.eps/4 \
            +(3*self.i.eps*f)/4 \
            -(3*self.m.eps*f)/4 \
            +(9*self.i.eps**2*f**2 \
            -6*self.i.eps**2*f \
            +self.i.eps**2 \
            -18*self.i.eps*self.m.eps*f**2 \
            +18*self.i.eps*self.m.eps*f \
            +4*self.i.eps*self.m.eps \
            +9*self.m.eps**2*f**2 \
            -12*self.m.eps**2*f \
            +4*self.m.eps**2)**(0.5)/4