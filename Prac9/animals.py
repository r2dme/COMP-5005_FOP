#Dog class

class Dog(): 
    myclass = "Dog"

    def __init__(self, name, dob, colour, breed): 
        self.name = name
        self.dob = dob 
        self.colour = colour 
        self.breed = breed
    
    def printit(self):
        print('Name: ', self.name) 
        print('DOB: ', self.dob) 
        print('Colour: ', self.colour) 
        print('Breed: ', self.breed) 
        print('Class: ', self.myclass)


#Cat Class

class Cat(): 
    myclass = "Cat"
    def __init__(self, name, dob, colour, breed):
        self.name = name
        self.dob = dob 
        self.colour = colour
        self.breed = breed
    def printit(self):
        print('Name: ', self.name) 
        print('DOB: ', self.dob) 
        print('Colour: ', self.colour)
        print('Breed: ', self.breed)


#Bird Class

class Bird(): 
    myclass = "Bird"

    def __init__(self, name, dob, colour, breed):
        self.name = name
        self.dob = dob          
        self.colour = colour
        self.breed = breed

    def printit(self):
        print('Name: ', self.name)         
        print('DOB: ', self.dob)          
        print('Colour: ', self.colour)
        print('Breed: ', self.breed)
