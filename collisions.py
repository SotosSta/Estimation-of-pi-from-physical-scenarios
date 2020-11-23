
"""
Tittle: Estimation of pi using elastic collisions.
Author: Sotirios Stamnas
Date: June 2020

An estimation for pi can be made by simulating elastic collision between two
blocks and a wall. The masses have to be chosen in an appropriate manner so that
the mass m2 is much bigger than m1. Also m1/m2 must be a power of 100. m1 has repeated collisions with m2 which 
bounces of a wall after every collision with m1. Using the conservation of 
energy, momentum and phase space representation of the results an estimation
for pi can be made (https://www.youtube.com/watch?v=jsYwFizhncE).

"""

import numpy as np
import matplotlib.pyplot as plt
m1 = 100**3 #kg
m2 = 1 #kg
v1 = -1 #m/s
v2 = 0 #m/s

v1_all = -1
v2_all = 0
number_of_collisions = 0


while v1<v2:
    
    v1 = (m1-m2)*v1/(m1+m2) + 2*m2*v2/(m1+m2)
    v1_all = np.vstack((v1_all,v1))

    v2 = (2*m1)*v1_all[-2]/(m1+m2) - (m1-m2)*v2/(m1+m2)
    v2_all = np.vstack((v2_all,v2))
    number_of_collisions +=1
    
    if v2<0:
        v1 = v1
        v1_all  = np.vstack((v1_all,v1))
        
        v2 = -v2
        v2_all  = np.vstack((v2_all,v2))
        number_of_collisions +=1
        
circle_radius = np.sqrt((m1*v1_all[0]**2+m2*v2_all[0]**2))
        
plt.figure(0)

plt.title('Phase space', size = 16)
plt.xlabel(r'$\sqrt{m _1} v_1$', size = 14)
plt.ylabel(r'$\sqrt{m _2} v_2$', size = 14)

plt.plot(circle_radius*np.cos(np.linspace(0,2*np.pi,10000)),
         circle_radius*np.sin(np.linspace(0,2*np.pi,10000)),color = 'black')

plt.plot(np.sqrt(m1)*v1_all,np.sqrt(m2)*v2_all, color = 'blue')
plt.plot([0,circle_radius],[0,np.sqrt(m2/m1)*circle_radius],color = 'red', label = 'End zone')
plt.plot([0,circle_radius],[0,0], color = 'red')
plt.legend()
plt.show()

print(r'$\pi$ = {0:1.4f}'.format(number_of_collisions/np.sqrt(m1/m2)))


