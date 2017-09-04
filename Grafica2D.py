# scatterplot.py
import numpy as np
import pylab as pl 
# Make an array of x values
x = [1, 2, 3, 4, 5, 6]
# Make an array of y values fro each x value
y = [7.66, 8.25, 9.00, 7.66, 8.60, 8.60]
# use pylab to plot x and y as cyan circle 
pl.plot(x, y, 'co')
# Inserta título en el eje y
pl.ylabel('Promedio')
# Inserta título en el eje x
pl.xlabel('Semestre')
# show the plot on the screen 
pl.savefig('semestrevspromedio.png')