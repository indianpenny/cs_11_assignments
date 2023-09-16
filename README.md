# cs_11_assignments

# **GUISnowman.py** 
This is a Python program that creates a simple graphical user interface (GUI) using the SimpleGUI library. The GUI draws a picture of Frosty's long-lost cousin, a winter-themed character. The code demonstrates how to use various drawing commands to create shapes such as circles, squares, triangles, and polygons. It also incorporates different colors and coordinates to compose the character's features. The resulting image is displayed in a frame with interative elements. Feel free to explore and modify this code to create your own custom GUI drawings or learn more about GUI development in Python. 

# **MountainPaths.py** 
Mountain Paths is a Python code designed to calculate a "greedy lowest-elevation-change walk" through a 2D grid of topographic data, simulating a path from one side of a map to the other. The objective is to find the route with the least change in elevation at each step.
The code includes an input image for displaying a map of Colorado. It draws a path on the map image loaded, illustrating a walk across Colorado using the described greedy algorithm.
To do that, the code utilizes the Matplotlib library for plotting and visualization. It reads topographic data from a file ("map.dat") and generates a visual representation of the calculated path on the map. The resulting image 
is saved as "contour.png."
Algorithm steps implemented:
Start in a cell at the left-most edge of the map (column 0).
In each subsequent column, take a "step" into one of the three adjacent cells, choosing the cell whose elevation is closest to the current cell's elevation.
In case of a tie between the forward position, proceed straight forward.
In case of a tie between the two non-forward positions, randomly choose the direction to go.
  
Feel free to explore this code to understand how it calculates and visualizes a path based on elevation changes and how it represents this path on the map of Colorado. You can also modify it for different map data and algorithms.

# **PlottingFunctions.py** 
This python code contains multiple plotting methods designed to plot four different types of math functions, each representing a relationship between two variables, on a 2x2 grid of graphs. The code calculates and generates data points for the following functions:
1. Payment vs. Amount Owed: This function calculates the total payment amount, including a 15% tip, based on the amount owed. It generates values for payments on amounts ranging from $20 to $100 in $5 increments.
2. Population vs. Time: This function calculates the population of Surrey, BC t years from now, assuming an initial population (P0) of 550,000 and a growth rate (r) of 9% (0.09). It generates values for the population from t = 0 to 20 years, using 2-year increments.
3. Current vs. Resistance: This function calculates the current (I) for a constant voltage (V) of 120 V, given varying resistance (R) values. It generates values for resistance from 100 Ω to 1000 Ω at intervals of 100 Ω.
4. Distance vs. Time: This function calculates the distance traveled by a ball thrown upward with an initial upward vertical velocity (v0) of 15 m/s and an acceleration (a) of -9.8 m/s^2. It generates values for distance from t = 0 to 10 seconds in 1-second increments.

The graphs are saved as an image file named "plot.png." This code is a useful example of how to generate data points for various mathematical functions and create a multi-graph visual representation of those functions. It can be customized to explore other mathematical relationships and plotting requirements. The resulting graph to visualize the relationships between the variables described by these functions.

# **LinearVsBinarySearchAnalysis.py** 
This python code is for analyzing linear and binary search algorithms. This creates two plots to compare the number of trials needed for different list lengths. It performs 1000 trials, each with a different list length, and records the number of attempts required to find a target number using both search methods. The code then plots this data on two separate graphs.
1. Linear Search Function:
The linear search function iterates through the list until it finds the target number. It keeps track of the number of attempts and appends this count to the count_l list.
2. Binary Search Function:
The binary search function performs a binary search on the sorted list to find the target number. It also keeps track of the number of attempts and appends this count to the count_b list.

Experimental Data:
The code runs a loop from 1 to 1000 trials, with each trial involving the following steps:
Generate a list of numbers from 1 to n in order.
Generate a random number from 1 to n as the target.
Perform both linear and binary searches on the list, recording the number of attempts needed to find the target.
Store the data (number of attempts) for each search in separate lists (count_l for linear search and count_b for binary search).
After all the trials are complete, the code plots each set of data on a separate graph using Matplotlib.
This code provides a visual comparison of the efficiency of linear search and binary search algorithms as the list length varies from 1 to 1000. 
The resulting graphs will help us understand how these search methods perform differently with changing list sizes.

# **Potions.py**
View Bubble Cup V9 D Potions Homework on dmoj.ca. 
This Python script is designed to help Harry Water, Ronaldo, Her-my-oh-knee, and their friends minimize the total time required to complete their Potions homework. Each student has a task with a certain difficulty level, and they aim to redistribute tasks to optimize their work based on their individual laziness levels. The goal is to find the shortest possible total time to complete all tasks while each student still does one task.

Problem Description:
Professor Snipe has assigned N tasks to the students, and each task has a difficulty level and corresponds to a student's laziness level. The time required for a student to finish a task is the product of their laziness level and the task's difficulty level. The students want to minimize the total time spent on all tasks.

Input:
The first line of input contains an integer N, representing the total number of tasks.
The next N lines each contain a single integer, representing the difficulty level of the task and the laziness level of the student initially assigned the task.

Output: 
The output should consist of a single line containing the minimum time needed to finish all tasks, modulo 10007.

Constraints
1 <= N <= 100,000
1 <= A[i] (difficulty/laziness level) <= 100,000

How to Use
Run the script in your Python environment.
Enter the number of tasks (N) when prompted.
Enter the difficulty level and laziness level for each task as per the prompts.
The script will calculate and display the minimum time required to complete all tasks.

Feel free to explore and use this code to help Harry Water, Ronaldo, Her-my-oh-knee, and their friends optimize their Potions homework. 

# **Scrabble.py**
This is a SCRABBLE game, each letter of the alphabet is assigned a specific point value. This program allows you to calculate the score of a word based on the sum of the point values of its individual letters. Additionally, you can find the highest-scoring word from a list of words.

The program consists of two main functions:
1. word_value(word): This function takes a word as a parameter and returns the calculated value of the word by adding up the values of its letters. The values of each letter are predefined in a dictionary.
2. best_word(words): This function takes a list of words as a parameter and uses the word_value function to determine which word has the highest score. It returns the word with the highest score.

The values assigned to each letter are as follows: 
dict_letters = {
    "A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4,
    "G": 2, "H": 4, "I": 1, "J": 8, "K": 5, "L": 1,
    "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1,
    "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8,
    "Y": 4, "Z": 10
}
Note: Make sure to input words in all capital letters.

Feel free to use this program to calculate the Scrabble score of words and find the highest-scoring word in a list!
