# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 00:04:56 2021

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.integrate import solve_ivp
from scipy.signal import find_peaks

def Virus_Transmission(t,data):
    S = data[0]
    I = data[1]
    R = data[2]


    
    dSdt = -beta*C*S*I
    dIdt = beta*C*S*I - gamma*I
    dRdt = gamma*I

    return [dSdt,dIdt,dRdt]

beta = 0.6 #Transmission Rate
gamma  = 0.2 # Recovery Rate
C = 1 #Restrictions

#Inital Condition 
S0 = 1 - 1/1000000
I0 =1/1000000
R0 = 0
data0 = [S0,I0,R0]

#Time Interval
day= 100
step = 1
t = np.linspace(0,day,day*step)



#Integrate
dataresult = solve_ivp(Virus_Transmission,(0,day),data0)

#Plot
t = dataresult.t
dataresult = dataresult.y
fgs = 20

fig,ax = plt.subplots(1,1,figsize=(fgs,fgs))
fig.tight_layout(pad = 7)
ax.plot(t,dataresult[1,:]*100)
ax.scatter(t,dataresult[1,:]*100)

ax.set_title(r"I vs time | $\beta$ = {0}  $\gamma$ = {1} Restrictions = {2} ".format(beta,gamma,C),fontsize=35)
ax.set(xlim=(0, max(t)), ylim=(0,100))
ax.set_ylabel('I(t)  %',fontsize=35)
ax.tick_params(axis='both', labelsize=25 )
ax.set_xlabel('Time (Day)',fontsize=35)
ax.set_aspect(max(t)/100)
#ax.legend()
ax.grid()



