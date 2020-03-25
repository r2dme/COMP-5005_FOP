#
# Author : Nishanth Prabu Bharathimohan 
# ID : 19733201
# # shrimpSimBase.py - Basic simulation of brine shrimp for assignment, S2 2019. 
#
# Revisions: 
#
# 30/10/2019 – Final version for assignment
#

import random
import matplotlib.pyplot as plt
import numpy as np
import time
import sys #Importing sys library to implement commandline arguments
from shrimptest import Shrimp


#Defining exhibit size
XMAX = 1000
YMAX = 500

# Process command line arguments
if (len(sys.argv) < 3):
    print('\nargv too short, usage: python3 <noOfSeaMonkeys> <simulationTime(Steps)\n')
    print('Using default values for noOfSeamonkeys (50) and simulationTime(10)\n')

    noOfSeaMonkeys = 50 # Total number of Sea Monkeys for test
    simulationTime = 10 # Time steps of simulation
else:
    noOfSeaMonkeys = int(sys.argv[1]) # Command line Sea Monkeys number input
    simulationTime = int(sys.argv[2]) # Command line Time steps calculation


# main function
def main():
    monkeys = []
    
    for i in range(noOfSeaMonkeys):
        randX = random.randint(0,XMAX)
        randY = random.randint(0,YMAX)
        monkeys.append(Shrimp([randX,randY]))
        #print(monkeys[i])
     
    for i in range(simulationTime):
        print("\n ### TIMESTEP ",i, "###")

#Defining 'buckets' for different states
        xvaluesEgg = []
        yvaluesEgg = []
        xvaluesHatch = []
        yvaluesHatch = []
        xvaluesJuve = []
        yvaluesJuve = []
        xvaluesAdult = []
        yvaluesAdult = []

#Defining 'sizes' for different states
        sizesEgg = []
        sizesHatch = []
        sizesJuve = []
        sizesAdult = []

        for m in monkeys:
          
            m.stepChange()
           #print(m)

            print("Shrimp details: Age-",m.age,"Other details- ",m)

            #Adding positional values and size of seamonkeys into their respective 'buckets'
            if m.state=='egg':
                xvaluesEgg.append(m.pos[0])
                yvaluesEgg.append(m.pos[1])
                sizesEgg.append(m.getSize())
            elif m.state=='hatchling':
                xvaluesHatch.append(m.pos[0])
                yvaluesHatch.append(m.pos[1])
                sizesHatch.append(m.getSize())
            elif m.state=='juvenile':
                xvaluesJuve.append(m.pos[0])
                yvaluesJuve.append(m.pos[1])
                sizesJuve.append(m.getSize())
            else:
                xvaluesAdult.append(m.pos[0])
                yvaluesAdult.append(m.pos[1])
                sizesAdult.append(m.getSize())

            #Reproduction - After two simulation time units of adult stage, it will start laying eggs for every four time steps

            if m.state == 'adult' and m.age in range(9,17,4): 
                monkeys.append(Shrimp([m.pos[0]-20,m.pos[1]-20]))

            #Adults die after 16 simulation time units and here they are changed to 'eggs' to show the same
            if m.state == 'adult' and m.age == 12:
                m.state = "egg"
                m.age = 0    

        #Adding a subplot and plotting multiple data points in the same plot 
        #(Reference: https://stackoverflow.com/questions/4270301/matplotlib-multiple-datasets-on-the-same-scatter-plot)

        fig = plt.figure()
        plt1 = fig.add_subplot(111)

        #Multiple plots with different identifiers according to the state
        #

        plt1.scatter(xvaluesEgg, yvaluesEgg,s=sizesEgg,color='red',marker='^')  
        plt1.scatter(xvaluesHatch,yvaluesHatch,s=sizesHatch,color='green',marker='x') 
        plt1.scatter(xvaluesJuve,yvaluesJuve,s=sizesJuve,color='black',marker='s') 
        plt1.scatter(xvaluesAdult,yvaluesAdult,s=sizesAdult,color='blue',marker='o')
 
        # Note plt origin is bottom left 
        plt.xlim(0,XMAX)
        plt.ylim(0,YMAX)
    
        # Save final plot image to current directory
        plt.savefig('shrimpSim_' + 'N' + str(noOfSeaMonkeys)+'_T' + str(simulationTime) + '.png')
        plt.show()
        time.sleep(0.1)

    
if __name__ == "__main__":
    main()
