"""
Created on Jan 31 14:37:20 2023

@author: Srishti
"""

#Use the demo code to create plots showing the number of trials for linear search vs binary #search for different list lengths. The two plots should show the number of tries needed to #find a number (y-axis) as a function of the length of the sequence (x-axis). 

#Add in a global count variable for each type of search and increment it inside the loops so #that it counts the number of tries needed to find a number. Test it to make sure it works!
#Outside of the search functions, create a loop that generates an integer n from 1 to 1000 to #get your experimental data by doing 1000 trials.

#Inside the loop:
#Generate a list of numbers from 1 to n in order (hint: list comprehension is helpful here!)
#Generate a random number from 1 to n as the target
#Perform a linear search and a binary search on the list of numbers, keeping track of the #number of attempts needed to find the number
#Store the data (number of attempts) for each search in two separate lists
#After all the trials are complete, plot each set of data on a graph

#For example, the first trial would be of length n=1. The list would be [1] and the target #would be a random number between 1 and 1 (so 1).  Each algorithm would take 1 try to find #the correct number. The second trial would be length 2 so the list would now be [1,2] and #the target will either be 1 or 2. The list and target will be sent to each search function #and they will either take 1 or 2 tries to find the target, etc.

# Compaing the graphs of Linear Search (linear trend) VS Binary Search (logarithmic trend) by # Srishti M

import matplotlib as mpl
import matplotlib.pyplot as plt
import random 
# Agg is used to create .png files
mpl.use('Agg')
# Create empty figure to plot graphs on
fig = plt.figure()

# FIX: Add in linear and binary search functions

count_l = [] # number of attempts needed for linear search to find target
count = 1 # initialize the count

def linear(list, target):
  global count, count_l
  for i in range(len(list)):  # increments through every single value in list until finds target
    if list[i] != target:  
      count += 1
      continue
    else:
      break
  count_l.append(count)
  count = 1
  return count_l

count_b = [] # number of attempts needed for binary search to find target
count2 = 1 # initialize the count2

def binary(list, target):
  global count2, count_b
  # initialize the first (left) and last (right) index (or positional) values of list
  left_index = 0
  right_index = len(list)-1
  while left_index <= right_index:
    mid_index = (left_index + right_index)// 2
    if list[mid_index] == target:
      break
    elif list[mid_index] < target:
      left_index = mid_index + 1
    else:
      right_index = mid_index - 1
    count2 += 1
  count_b.append(count2)
  count2 = 1
  return count_b 

list = [] # send this list as the parameter for the functions
listval = 0 # to initialize first value that will go through loop and into the list

for h in range(1, 1001): #to get 1000 trials worth of data
  listval += 1
  list.append(listval)
  # list starts with [1] and then increases length by appending the next number [1,2]...
  target = random.randint(1, len(list)) 
  # single new random target value anywhere between 1 to last value of the list (this is what causes the sudden rise and falls in the graph)
  linear(list, target)
  binary(list, target)
  #call functions using the parameters above

# Add subplots using add_subplot(rows,cols,number)
grid1 = fig.add_subplot(1,2,1)
grid2 = fig.add_subplot(1,2,2)
# Add data to grids
grid1.plot(list, count_l)    
grid2.plot(list, count_b)    
# Save graphs to .png file
fig.savefig('graph.png')