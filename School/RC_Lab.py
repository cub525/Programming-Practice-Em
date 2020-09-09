import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

file = 'rc_lab_1_datonly.csv'
C = .1 #Farad
r = 973 #ohm
def solve_lab(data,r,C):
    data = np.genfromtxt(data, dtype = 'float',
                         names = True,delimiter=',')
    lnvolts = [np.log(data['Voltage'][0]/float(i)) for i in data['Voltage']]
    slope, intercept, r_value, p_value, std_err = stats.linregress(data['Time'], lnvolts)
    percenterror = round(100*abs(r*C-(slope**-1))/(r*C),3)
    rsqrd = round(r_value**2, 3)
    
    plt.plot(data['Time'],lnvolts,marker='.',linestyle='none',label = 'Scatter plot of data')
    plt.plot(data['Time'], np.poly1d(np.polyfit(data['Time'], lnvolts, 1))
    (data['Time']),label='Best fit line\nr^2={0}\npercent error = {1}%'.format(rsqrd,percenterror))
    plt.plot(0,0,color='w',label = 'r = {0}\nC = {1}'.format(r,C))
    plt.ylabel('Natural log of voltage')
    plt.xlabel('Time')
    plt.title('Emmett Hart RC Lab: Ln Voltage vs Time')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    solve_lab(file,r,C)