#
# strings2.py: Read in a string and print it forward
#              using a loop and a method call

instring = input('Enter a string... ')
# *** add upper and duplicating code here

instring = instring.upper()
instring = instring*2

# Print forward with a while loop

print('String is : ',end='')
index = 0
while index < len(instring)-1:
    print (instring[index], end='')
    index = index+2
print()

# Print forward with a range loop

print('String is :', end='')
for index in range (0, len(instring)-1,2):
    print(instring[index], end='')
print()

# Print forward with slicing

print('String is :', instring[::2])
