# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 20:42:45 2020

@author: EOL
"""

import matplotlib.pyplot as plt
import math
#All units are in base metric unless stated otherwise, millimeters will be used for
dt = .0001 #Seconds
l = .61 #Length of rails
rc = 1.68e-8 * 5.938e-6 * .25 # resistivity of copper or other material
rp = .001 #Resistiviy of projectile
C = 1 #Equivalent Capacitence of capacitors
m = .01 #mass of projectile




x=0
xl = [x]
xd = 0
xld = [xd]
lt = [0]
t = 0
ltrue = []
r = .0001
lr = [r]
v = 2.7
lv = [v]
xdd = 4e-7*(v/r)**2
xldd = [float('Nan')]
try:
    while t<10 and x<.61:
        xd = xdd*dt + xd
        x = xd*dt + x
        xdd = x**-2*.5*math.log(x**2+l**2)+l-math.log(x)
        xl.append(x)
        xld.append(xd)
        xldd.append(xdd)
        t = t+dt
        lt.append(t)
except KeyboardInterrupt:
    pass
lv = [math.sqrt((C*v-(m*xd**2))/C) for xd in xld]
dv = lv[-1] - lv[0]
print(dv)
plt.plot(lt,xl,label = 'position')
plt.plot(lt,xld, label = 'velocity')
plt.plot(lt,xldd, label = 'acceleration')
plt.legend()