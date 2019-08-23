#
# growth.py: Simulating unconstrained growth
#

print('\n Simulation - Unconstrained Growth \n' )

print('Enter Simulation Length: ')
sim_len = int(input())

print('Enter Population: ')
pop = int(input())

print('Enter Growth Rate: ')
growth_rate = int(input())

print('Time: ')
time_len = int(input())

num_iter = sim_len*time_len
print('Number of iterations: ',num_iter)

growth_step = growth_rate*time_len
print('Growth rate  per time: ',growth_step)

for i in range(1,int(num_iter)-1):
	growth = growth_step*pop
	population = pop+growth
	time = i*time_len

print('Time: ',time,'\nGrowth: ',growth,'\nPopulation: ',population)



