# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 23:12:12 2014

@author: Jussi Tiira
"""

from ParticleRange import ParticleRange

mi = complex(1.310990,3.11e-9)
ma = complex(1.57,0.007)

#ice: crap in, sensible output; sensible input, crap out
ice_vis = ParticleRange(1e2/3000,1e3/300,mi,name='ice particles, short wavelenght')
ice_rad = ParticleRange(1e2/3e8,1e3/1e6,mi,name='ice particles, long wavelenght')
aer = ParticleRange(10/3e3,5e3/3e2,ma,name='mineral dust / aerosols')
ice_c = ParticleRange(1e4,1e6,mi,wavelength=532,name='ice particles')
aer_c = ParticleRange(600,5000,mi,wavelength=532,name='mineral dust / aerosols')

ptypes = [ice_vis,ice_rad,aer]
cptypes = [ice_c,aer_c]

for ptype in ptypes:
    ptype.plot_eff()
    ptype.plot_ratio()
    ptype.plot_error() #not working?

# not working?    
#for cptype in cptypes:
#    cptype.plot_ratio()
#    cptype.plot_error()