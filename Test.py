# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 12:42:52 2015

@author: Chris

"""

import scipy as sc
import matplotlib.pyplot as plt

x = sc.arange(0, 5*sc.pi, 0.1);
y = sc.sin(x)
plt.plot(x, y)

z = sc.cos(x)
plt.plot(x, z)

a = sc.tan(x)

plt.plot(x,a)

plt.axis([0,5*sc.pi,-1,1])