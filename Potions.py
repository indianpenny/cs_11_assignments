"""
Created on Feb 1 15:37:20 2023

@author: Srishti
"""

#Potions Homework code by Srishti M. 

n = int(input().strip())
if not (1 <= n <= 100000):
    print("Invalid input values")
    exit()

task_difficulty = [int(input().strip()) for i in range(n)]
for i in range(len(task_difficulty)):
  if not (1 <= task_difficulty[i] <= 100000):
      print("Invalid input values")
      exit()

def minimum_time_to_finish_tasks(n, task_difficulty):
    
  task_difficulty.sort()
  total_time = 0
  for i in range(n):
      total_time += task_difficulty[i] * task_difficulty[n - i - 1]
  return total_time % (10**9 + 7)

print(minimum_time_to_finish_tasks(n, task_difficulty))