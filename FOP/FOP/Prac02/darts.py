import random

num_trials = 1000000

ncirc = 0
r = 1.0
r2 = r*r

for i in range (num_trials):
    x = random.random();
    y = random.random();
    if ((x*x + y*y) <= r2):
        ncirc += 1

pi = 4.0 * ncirc / num_trials

print ("\n For", num_trials, " trials, pi = ",pi)


