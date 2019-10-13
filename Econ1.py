# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:34:06 2019

@author: EOL
"""

import matplotlib.pyplot as plt
import math
\
#def Econ_plots(fc,vc,p):
vc = 5
fc = 10
vcl = []
avc = []
afc = []
atc = []
tc = []
output = []
mc = []
r = 10
p1 = []
p2 = []
for i in range(r):
    p1.append(1.2)
    p2.append(3.6)
    vcl.append((i-3)**2*(i+4)*.1+4)
    try:
        afc.append(fc / (i))
        avc.append(vcl[i]/i)
    except ZeroDivisionError:
        afc.append(math.nan)
        avc.append(math.nan)
        pass
    
    tc.append(vcl[i] + fc)
    output.append(i)
    try:
        atc.append(afc[i] + avc[i])
    except TypeError:
        atc.append(math.nan)
        pass    
mc.append(math.nan)
for i in range(1,r):
    mc.append(tc[i]-tc[i-1])
plt.plot(output,avc,output,atc,output,mc,output,p1,output,p2)
plt.title('Chart Showing Results on a firm over a change in price')
plt.xlabel('Quantity')
plt.ylabel('Price')
plt.legend(['AVC','ATC','MC','P1','P2'])
#if __name__ == '__main__':
#    Econ_plots(10,5,15)