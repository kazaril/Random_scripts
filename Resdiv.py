#!/usr/bin/env python

import sys

best=100

if len(sys.argv) != 3:
        print('use in the following way: Resdiv.py Vi Vo')
        sys.exit() 


Vi=float(sys.argv[1])
Vo=float(sys.argv[2])


if Vo > Vi:
        print('Are you really trying to INCREASE the voltage with a divider? You need some negative resistors')
        sys.exit() 

BMDres=[0.01,0.1,0.05,0.15,0.25,1,1e3,1e6,1.1e3,1.2e3,1.8e3,1.62e3,2.2,2.2e3,2.7e3,3e6,3.3,3.16e3,3.24e3,4.7,4.7e3,5.6,6.81e3,7.68e3,8.06e3,8.45e3,10,10e3,12.1,14e3,16.7,18,23.7e3,27,27e3,33,36,37.4,39,43.2,47e3,49.9,51,56,56e3,68,75,86.6,100,100e3,120e3,150,180,180e3,196,220e3,240,270e3,316,330,470,470e3,510,511,560e3,680,750,6996e6]

for i in range(0,len(BMDres)):
        for j in range(0,len(BMDres)):
                a=Vi*(BMDres[i]/(BMDres[i]+BMDres[j]))
                err=abs(Vo-a)
                if err <= best:
                        best = err
                        Ra = BMDres[i]
                        Rb = BMDres[j]
                 
        

S= 'Ra = '+str(Ra)+' Ohms'
print(S)
S= 'Rb = '+str(Rb)+' Omhs'
print(S)
S= 'Error is '+str(best)+' V'
print(S)

