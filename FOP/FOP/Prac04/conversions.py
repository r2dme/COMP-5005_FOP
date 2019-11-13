#  
# conversions.py – module with functions to convert between units #
# fahr2cel : Convert from Fahrenheit to Celsius.
#

def fahr2cel(fahr):
    celsius = (fahr - 32) * (5/9) 
    return celsius

def kel2cel(kel):
    celsius = kel + 273.15
    return celsius

def cel2kel(cel):
    kelvin = celsius + 273.15
    return kelvin

def cel2fahr(cel):
    fahr = (cel * 9/5) + 32
    return fahr


