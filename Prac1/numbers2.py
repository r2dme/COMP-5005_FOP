#
# numbers2.py: Read in ten numbers and give sum of numbers
#

print('Enter ten numbers...')
total=0

for i in range(10):
	print('Enter a number (',i+1, ')...')
	number = int(input())
	total = total+number

print('Total is ',total)


