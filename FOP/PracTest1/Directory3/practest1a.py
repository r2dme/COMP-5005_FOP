#
# Student Name: Nishanth Prabu Bharathimohan
# Student ID: 19733201
#
# practest1a.py: Read in a string and print it 
#

instring = input('Enter a string..')

instring = instring.upper()

print('The string is : ')

for i in range (2,len(instring),2):
    print(instring[i], end='')

print()


