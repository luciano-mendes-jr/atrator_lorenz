#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from matplotlib.animation import FuncAnimation 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from numpy import arange 

def update(i):
    ax.clear()
    ax.view_init(30, -10+i/2) #rotaciona o eixo 
    ax.grid(False)
    ax.plot(xi[0:i], yi[0:i], zi[0:i], color = 'orange')
    ax.scatter(xi[i], yi[i], zi[i],s = 20, marker = 'o', c ='w')

plt.style.use(['dark_background'])
fig = plt.figure(dpi = 100)  
ax = fig.add_subplot(projection = '3d')

xi, yi, zi = [] , [], []

#condições iniciais + passo de integração. 
x ,y , z, dt  = 1.0 , 1.0, 0.0, 0.015

#constantes 
b ,r , s = 8.0/3.0 , 28.0, 10.0

t = arange(dt,50+dt,dt)

ax.w_xaxis.pane.fill = False
ax.w_yaxis.pane.fill = False
ax.w_zaxis.pane.fill = False

for i in range(len(t) - 1):
    xi.append(x)
    yi.append(y)
    zi.append(z)
    x = x + (s*y - s*x)*dt
    y = y + (r*x- y - x*z)*dt
    z = z + (x*y - b*z)*dt
   
ani = FuncAnimation(fig,update,arange(len(t)),interval = 0,repeat = False)   
plt.show()
 


