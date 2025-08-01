import numpy as np
import matplotlib.pyplot as plt

size = 10_000 #number of dice throws

#simulate throw of two dice
dice_roll_1 = np.random.randint(1,7, size=size) 
dice_roll_2 = np.random.randint(1,7, size=size) 
sums = dice_roll_1 + dice_roll_2

#compute probability of each sum
values , counts = np.unique(sums, return_counts = True) 
probabilities = counts/size

#plot of the histogram with results
plt.bar(values, probabilities)
plt.xlabel('Sum of two dice')
plt.ylabel('Probability')
plt.title(f'Distribution of Dice Sums ({size} rolls)')
plt.show()

#calculate mean and varience
mean = np.mean(sums) 
variance = np.var(sums) 

print(f'The mean of the throws is {mean :.2f} and the variance is {variance :.2f}')