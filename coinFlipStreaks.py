# The Coin Flip Streak 1-4B
# Training project from automateTheBoringStuff.com

# Write a program to find out how often a streak of 
# six heads or a streak of six tails comes up in a 
# randomly generated list of heads and tails. Your 
# program breaks up the experiment into two parts: 
# the first part generates a list of randomly 
# selected 'heads' and 'tails' values, and the 
# second part checks if there is a streak in it. Put 
# all of this code in a loop that repeats the 
# experiment 10,000 times so we can find out what 
# percentage of the coin flips contains a streak of 
# six heads or tails in a row.

import random
numberOfStreaks = 0
outcomeTuple=('T','H') # 0 for Tails, 1 for Heads

for experimentNumber in range(10000) :
    # Code that creates a list of 100 'heads' or 'tails' values.


    myOutcome="" # set empty string to record outcomes for each 100 flip run
    for i in range(100) : #'flip' 100 times
        myOutcome += outcomeTuple[ int(random.random()+.5) ] # 0/T for Tails, 1/H for Heads
    
    # Code that checks if there is a streak of 6 heads or tails in a row.
    if ("HHHHHH" in myOutcome) or ("TTTTTT" in myOutcome) : # 1 or more 6 streak appeared
        numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))