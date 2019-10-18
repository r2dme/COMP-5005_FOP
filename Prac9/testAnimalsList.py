from animals import Dog
from animals import Cat
from animals import Bird

fileobj = open('animals.csv','r')

data = fileobj.readlines()

fileobj.close()

for line in data:
    
    splitline = line.split('=')
    






