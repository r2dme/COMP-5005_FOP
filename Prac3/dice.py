import matplotlib.pyplot as plt
import random

dice = ['one','two','three','four','five','six'] 
one, two, three, four, five, six = 0,0,0,0,0,0

trials = 1000 

print('\nDICE TOSS\n')

for index in range(trials):
    choice = random.choice(dice) 
    if choice == 'one':
        one += 1 
    elif choice == 'two':
        two += 1 
    elif choice == 'three':
        three += 1 
    elif choice == 'four': 
        four += 1 
    elif choice == 'five':
        five += 1
    else:
        six += 1

print('\nRESULTS\n') 
print('1: ', one) 
print('2: ', two) 
print('3: ', three) 
print('4: ', four) 
print('5: ', five) 
print('6: ', six)

#plot
plt.title('Roll the Dice') 
plt.xlabel('Number') 
plt.ylabel('Count')
plt.bar([1, 2, 3, 4, 5, 6],[one, two, three, four, five, six], 0.9, color='purple')

plt.show()
