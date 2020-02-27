import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

data = np.genfromtxt('rc_lab_1_datonly.csv', dtype = 'float',
                     names = True,delimiter=',')
C = .1 #Farad
r = 973 #ohm

lnvolts = [np.log(data['Voltage'][0]/i) for i in data['Voltage']]
slope, intercept, r_value, p_value, std_err = stats.linregress(data['Time'], lnvolts)
percenterror = round(100*abs(r*C-slope**-1)/r*C,3)
rsqrd = x = round(r_value**2, 3)

plt.plot(data['Time'],lnvolts,marker='.',linestyle='none',label = 'Scatter plot of data')
bestfit = plt.plot(data['Time'], np.poly1d(np.polyfit(data['Time'], lnvolts, 1))
(data['Time']),label='Best fit line \n r^2={0} \n percent error = {1}%'.format(rsqrd,percenterror))
plt.legend()