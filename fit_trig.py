#FitTrig.py
import numpy as np
import matplotlib.pyplot as plt

#Load Raw Data
x_data = np.array([0,15,30,45,60,75,90,105,120,135,150,165,180]) #Control Drum Orientation
y_data = np.array([0.90480,0.90451,0.90465,0.90540,0.91043,0.92393,0.94719,0.97567,1.00105,1.02166,1.03612,1.04500,1.04769]) #Keff
stdev = np.array([0.00022,0.00020,0.00021,0.00021,0.00020,0.00022,0.00021,0.00021,0.00020,0.00021,0.00021,0.00020,0.00021]) #Keff

trunc_low = 3
trunc_high = 1

#Define Functions
def truncate(array):
    if trunc_low!=0:
        array=np.split(array,[trunc_low])[1]
    if trunc_high!=0:
        array=np.split(array,[-trunc_high])[0]
    return array

def crit_to_reac(crit):
    reac=np.log(crit)
    #reac=(crit-1)/crit
    return reac

def cos(x, a, b, c, y0):
    return y0 + (a * np.cos(b * x + c))

def sin(x, a, b, c, y0):
    return y0 + (a * np.sin(b * x + c))

#Truncate Data
x_data = truncate(x_data)
y_data = truncate(y_data)
stdev = truncate(stdev)

#Transform Data
y_data=crit_to_reac(y_data)

#Describe Curve (cosine)
y_max=max(y_data)
y_min=min(y_data)
per = ((x_data[-1]-x_data[0])/180)*(2*np.pi)
phase = np.deg2rad(x_data[0])

#Define Parameters
a = -(y_max-y_min)/2
b= 2*np.pi/per
c=b*phase
y0=y_data[0]-a

#Curve
y_calc= cos(np.deg2rad(x_data), a, b, c, y0)

rd=5
equation = str(round(y0,rd)) + "+" + str(round(a,rd)) + "cos(" + str(round(b,rd)) + "x +" + str(round(c,rd)) + ")"

#Plot
plt.figure()
#plt.title(equation)
plt.xticks(x_data)
plt.ylim(-0.11,0.11)
plt.ylabel("ϱ")
plt.xlabel("Control Drum Orientation (°)")
plt.scatter(x_data, y_data, label='MCNP Data')
plt.plot(x_data, y_calc, label='Fitted Curve')
plt.legend(loc='upper left')
plt.plot(x_data,np.zeros(len(x_data)),'k:')
plt.show()
