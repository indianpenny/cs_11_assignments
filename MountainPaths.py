"""
Created on Jan 21 14:37:20 2023

@author: Srishti
"""

#When traveling through mountains you want to take the route that requires the least change in elevation with each step you take. Given some topographic data it should be possible to calculate a greedy lowest-elevation-change walk from one side of a map to the other.

#For a 2D grid, we can envision a "walk" as starting in some cell at the left-most edge of the map (column 0) and proceeding forward by taking a "step" into one of the 3 adjacent cells in the next column over (column 1). Our "greedy walk" will assume that you will choose the cell whose elevation is closest to the elevation of the cell you're standing in. (NOTE: this might mean walking uphill or downhill).

#In the case of a tie with the forward position, you should always choose to go straight forward.  In the case of a tie between the two non-forward locations, you should randomly choose where to go.

import matplotlib as mpl
import matplotlib.pyplot as plt
import random

X = [i for i in range(480)]
Y = [j for j in range(480)]
Z = []

f = open("map.dat")
for line in f:
    row = line.split()
    row = list(map(int, row))
    Z.append(row)

fig = plt.figure()
cp = plt.contourf(X, Y, Z, 20, cmap='magma')
plt.colorbar(cp)

xs = [i for i in range(480)]
ys = []

# FIX: Change random to greedy alg
#print(Z[0][2]) # Z[row][col] or Z[y][x]

y = random.randrange(480)
print("starting at x = 0 and y =",y)
ys.append(y)
for x in xs:
    if x == 479:
      break
    if y == 479:
      break

    diff_f = abs(Z[y][x + 1] - Z[y][x])
    diff_up = abs(Z[y-1][x + 1] - Z[y][x])
    diff_down = abs(Z[y+1][x + 1] - Z[y][x])
    
    if diff_f < diff_up and diff_f < diff_down:
      #y_tmp = Z[y][x + 1]
      y = y
    else:
      if diff_up == diff_down:
         #y_tmp = Z[y+1][x + 1]
         y = y +1
      elif diff_up > diff_down:
         #y_tmp = Z[y+1][x + 1]
         y = y +1
      elif diff_up < diff_down:
         #y_tmp = Z[y-1][x + 1]
         y = y-1

    ys.append(y)

plt.plot(xs, ys, 'g.')
mpl.use('Agg')
fig.savefig('contour.png')
