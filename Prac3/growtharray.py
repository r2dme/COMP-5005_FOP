
# growtharray.py - Using arrays to store growth values and plot the arrays #

import matplotlib.pyplot as plt
import numpy as np

timevalues = np.zeros(100)
popsvalues = np.zeros(100)

print("\nSIMULATION - Unconstrained Growth\n") 

length = 100
population = 100
growth_rate = 0.1
time_step = 0.5
num_iter = length / time_step
growth_step = growth_rate * time_step

print("INITIAL VALUES:\n")
print("Simulation Length (hours): ", length)
print("Initial Population: ", population)
print("Growth Rate (per hour): ", growth_rate)
print("Time Step (part hour per step): ", time_step)
print("Num iterations (length * timestep / hour):",num_iter) 
print("Growth step (growthrate per timestep):",growth_step)
print("\nRESULTS:\n")
print("Time: ", 0, " \tGrowth: ", 0, " \tPopulation: ", 100)

times=[0]
pops=[100]

for i in range(1, int(num_iter) + 1 ):
	growth = growth_step * population
	population = population + growth
	time = i * time_step
	times.append(times)
	pops.append(population)

timevalues = np.array(times)
popsvalues = np.array(pops)

print("Time: ", time, " \tGrowth: ", growth," \tPopulation: ", population)
print("\nPROCESSING COMPLETE.\n")

plt.title('Prac3.1: Unconstrained Growth')
ply.xlabel('Time') 
plt.plot(timevalues,popsvalues,'r-')
plt.show()
