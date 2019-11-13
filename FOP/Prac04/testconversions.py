#
# testConversions.py - tests the functions in conversions.py
#

from conversions import *

print("\nTESTING CONVERSIONS\n")

testF = 100
testC = fahr2cel(testF)

print("Fahrenheit is ", testF, " Celsius is ", testC) 
print()


testC = 37.7
testF = cel2fahr(testC)

print("Celsius is ",testC,"Fahrenheit is ",testF)
print()


