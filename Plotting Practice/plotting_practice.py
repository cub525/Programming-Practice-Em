# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:17:37 2019

@author: EOL
"""
import numpy as np
import matplotlib.pyplot as plt
data = np.genfromtxt('Plotting_for_python.csv', dtype = 'float',
                     names = True,delimiter=',')

plt.plot(data['Time'],data['Temp'])
plt.show()