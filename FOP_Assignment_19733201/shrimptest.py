
# Author : Nishanth Prabu Bharathimohan
# ID : 19733201
#
# shrimp.py - Class definitions for simulation of brine shrimp 
#
# Revisions: 
#
# 30/10/2019 – Final version for assignment
#


#importing random library to use random numbers

import random

class Shrimp():
    time2hatch_egg = 2
    time2grow_hatch = 4
    time2grow_juvie = 6

    states = ["egg","hatchling","juvenile","adult"]
    
    def __init__(self, pos):
        self.pos = pos
        self.state = self.states[0]
        self.age = 0
        
    def __str__(self):
        return self.state + " @ " + str(self.pos)
    
    def stepChange(self):

        self.age += 1
         
        #Assigning movement data according to the state
        if self.state == "egg":
            self.pos[1] += random.randrange(-15,15,1)
            self.pos[0] += random.randrange(-15,15,1)

            #Moving seamonkeys when they go near the habitat boundaries 
            if self.pos[0]<=0 or self.pos[1]<=0:   
                self.pos[0]+= random.randrange(10,15,1)
                self.pos[1]+= random.randrange(8,12,1)

            if self.pos[0]>=1000 or self.pos[1]>=500:
                self.pos[0]-= random.randrange(10,15,1)
                self.pos[1]-= random.randrange(10,15,1)

            if self.age > self.time2hatch_egg:
                self.state = "hatchling"
        
        elif self.state == "hatchling":
            self.pos[1] += random.randrange(-25,25,1)
            self.pos[0] += random.randrange(-25,25,1)

            if self.pos[0]<=0 or self.pos[1]<=0:
                self.pos[1] += random.randrange(15,25,1)
                self.pos[0] += random.randrange(9,19,1)

            if self.pos[0]>=1000 or self.pos[1]>=500:
                self.pos[0]-= random.randrange(25,30,1)
                self.pos[1]-= random.randrange(20,30,1)

            if self.age > self.time2grow_hatch:
                self.state = "juvenile"

        elif self.state == "juvenile":
            self.pos[1] += random.randrange(-40,40,1)
            self.pos[0] += random.randrange(-40,40,1)

            if self.pos[0]<=0 or self.pos[1]<=0:
               self.pos[1] += random.randrange(20,40,1)
               self.pos[0] += random.randrange(18,28,1)

            if self.pos[0]>=1000 or self.pos[1]>=500:
                self.pos[0]-= random.randrange(30,40,1)
                self.pos[1]-= random.randrange(30,40,1)              

            if self.age > self.time2grow_juvie:
                self.state = "adult"

        else:
            xmov = random.randrange(-60,60,1)
            ymov = random.randrange(-35,35,1)
            self.pos[0] += xmov
            self.pos[1] += ymov
            
            if self.pos[0]<=0 or self.pos[1]<=0:
                self.pos[1] += random.randrange(30,60,1)
                self.pos[0] += random.randrange(25,35,1)

            if self.pos[0]>=1000 or self.pos[1]>=500:
                self.pos[0]-= random.randrange(20,80,1)
                self.pos[1]-= random.randrange(20,50,1)
                
                       
    def getSize(m):
        if m.state == "egg":
            size = 10
        
        elif m.state == "hatchling":
            size = 15

        elif m.state == "juvenile":
            size = 25

        else:
            size = 50
        return size


