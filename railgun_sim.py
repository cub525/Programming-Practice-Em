# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:45:16 2020

@author: EOL
"""
import matplotlib.pyplot as plt
#All units are in base metric unless stated otherwise
dt = .0001
d = .02 #Distance between rails
Bex = 0 # Additional Magnetic field
l = 1 #Lengthe of wire
rw = 0 #Will be implemented later, resistivity of copper or other material
rp = 1 #Resistiviy of projectile
C = 200 #Equivalent Capacitence of capacitors
V = 10 #Equivalent voltage of capacitors
esr = .00001 #ESR of capacitors
m = .015 #mass of projectile

I = 10 #Amperage in the wires, might become iterable







#x=1
#xl = []
#xd =0
#xld = []
#xdd = 0
#xldd = []
#lt = []
#t = 0
#ltrue = []
#try:
#    while t<10:
#        xdd = 1/x
#        xd = xdd*dt + xd
#        x = xd*dt + x
#        xl.append(x)
#        xld.append(xd)
#        xldd.append(xdd)
#        t = t+dt
#        lt.append(t)
#except KeyboardInterrupt:
#    pass
#plt.plot(lt,xl,lt,xld,lt,xldd)