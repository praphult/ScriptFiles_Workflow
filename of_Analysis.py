"""
Python script file to perform analysis 
on the test case in openFOAM 

Test case : 3D Heat conduction Manufactured
            Solution 

Created by : Praphul 

Date : 09-Aug-2019

Pre-requisites : csv datafiles in format 'SolutionData_nXnXn.csv' format
where n is the grid size

"""

import re 
import glob, os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

files = sorted(glob.glob1(os.getcwd(),'*.csv'))

db = {} #Database
gn = {} #Gridnames


n = len(files) 

cols = ["Temp","vtk", "arc", "x" ,"y" ,"z"] 

i = 0 
for j in files:
    i = i + 1 
    key_name = "D"+str(i) 
    db[key_name] = pd.read_csv(j, skiprows = 1, names = cols)
    gn[key_name] = re.split('_|\.',j) #<------Ref no. 1)

#Theoertical calculations <------- Users can edit the following block
x = np.linspace(0,0.01,1001) 
y = np.linspace(0,0.01,1001) 
z = np.linspace(0,0.01,1001) 

arc = np.sqrt(x**2 + y**2 + z**2) 

T_theo = 5.0 * np.sin(np.square(arc)) 

#<-------------------------------- Till here

plt.close('all')
plt.figure()
plt.plot(db['D1'].arc, db['D1'].Temp, '-.k', label = gn['D1'][1])
plt.plot(db['D2'].arc, db['D2'].Temp, ':k', label = gn['D2'][1])
plt.plot(db['D3'].arc, db['D3'].Temp, '--k', label = gn['D3'][1])
plt.plot(arc,T_theo, '-k', label = 'Theoretical') 
plt.legend()
plt.xlabel('Distance, (m)')
plt.ylabel('Temperature, T (K)')
plt.xscale('log')
plt.yscale('log')
plt.savefig('P_42_OF_TempVariation_log.eps') 
#plt.close() 


plt.figure()
plt.plot(db['D1'].arc, db['D1'].Temp, '-.k', label = gn['D1'][1])
plt.plot(db['D2'].arc, db['D2'].Temp, ':k', label = gn['D2'][1])
plt.plot(db['D3'].arc, db['D3'].Temp, '--k', label = gn['D3'][1])
plt.plot(arc,T_theo, '-k', label = 'Theoretical') 
plt.legend()
plt.xlabel('Distance, (m)')
plt.ylabel('Temperature, T (K)')
plt.savefig('P_42_OF_TempVariation.eps') 


# REFERENCES 


# 1)  Extracts the grid terminology i.e extracts 10x10x10 from file name SolutionData_10X10X10.csv

