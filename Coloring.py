# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 02:57:06 2020

@author: 90538
"""
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import colors

import numpy as np

from PIL import Image

data = np.random.rand(10, 10) * 20
image = Image.open('mapsPY.png')
# create discrete colormap
cmap = colors.ListedColormap(['red', 'blue'])
bounds = [0,10,20]
norm = colors.BoundaryNorm(bounds, cmap.N)

my_dpi=50.
fig=plt.figure(figsize=((float(image.size[0])/my_dpi),(float(image.size[1])/my_dpi)),dpi=my_dpi)
ax=fig.add_subplot(111)



fig, ax = plt.subplots()
ax.imshow(data, cmap=cmap,norm=norm)

# draw gridlines
ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
#ax.set_xticks(np.arange(0, image.size[0], 1));
#ax.set_yticks(np.arange(0, image.size[1], 1));

#fig = pylab.figure()


matplotlib.rc('axes',edgecolor='b')
plt.plot([0, 1], [0, 15], linewidth=20)
plt.plot([0, 15], [2, 1])
plt.plot([12,1], [20, 10], linewidth=20)
plt.plot([20,10], [20, 15], linewidth=20)
plt.savefig('test.png')

plt.show()