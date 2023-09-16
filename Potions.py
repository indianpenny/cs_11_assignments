"""
Created on Feb 1 15:37:20 2023

@author: Srishti
"""

n = int(input().strip())

if not (1 <= n <= 100000):
    print("Invalid input values")
    exit()

task_difficulty = [int(input().strip()) for i in range(n)]

if any(not (1 <= x <= 100000) for x in task_difficulty):
    print("Invalid input values")
    exit()

def minimum_time_to_finish_tasks(n, task_difficulty):
    task_difficulty.sort()
    total_time = 0
    for i in range(n):
        total_time += task_difficulty[i] * task_difficulty[n - i - 1]
    return total_time % 10007

print(minimum_time_to_finish_tasks(n, task_difficulty))
