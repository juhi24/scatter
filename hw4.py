# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 14:27:36 2014

@author: jussitii
"""

class Mixture:
    
    def __init__(self,eps_m,eps_i,rho_m,rho_i):
        self.eps_m = eps_m
        self.eps_i = eps_i
        self.rho_m = rho_m
        self.rho_i = rho_i
        
    def fraction(self,rho):
        return (rho - self.rho_m)/(self.rho_i - self.rho_m)
        
    def max_gar(self,rho):
        f = self.fraction(rho)
        eps_diff = self.eps_i - self.eps_m
        return self.eps_m + \
            3*f*self.eps_m*(eps_diff)/(self.eps_i+2*self.eps_m-f*(eps_diff))

    def bruggeman(self,rho):
        f = self.fraction(rho)
        return self.eps_m/2 \
            -self.eps_i/4 \
            +(3*self.eps_i*f)/4 \
            -(3*self.eps_m*f)/4 \
            +(9*self.eps_i**2*f**2 \
            -6*self.eps_i**2*f \
            +self.eps_i**2 \
            -18*self.eps_i*self.eps_m*f**2 \
            +18*self.eps_i*self.eps_m*f \
            +4*self.eps_i*self.eps_m \
            +9*self.eps_m**2*f**2 \
            -12*self.eps_m**2*f \
            +4*self.eps_m**2)**(0.5)/4