#
# numbers3.py: Read in a list of numbers (negative to exit) and  
#              give the sum of the numbers

count = 0
total = 0
print("Enter a list of numbers, negative to exit...")
number = int(input())

while number >=0:
    count += 1      #equivalent to count = count+1
    total += number #equivalent to total = total + number
    print("Next number..")
    number = int(input())

print("Total is ", total, "and count is ", count)

