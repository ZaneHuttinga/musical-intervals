# Import modules
import pandas as pd
import random

# Pull data from CSV file
basic = pd.read_csv('intervals.csv', usecols=[*range(0,7)])

# Create list of root notes from first column of pandas dataframe 'basic'
first = list(basic.iloc[0:7,0])

# Create list of possible intervals
intervals = ['second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

# Define function that runs the quiz
def quiz():
    # Select random root note
    root_note = random.choice(first)
    # Find index of root note in first column of dataframe
    for i in range(7):
        if root_note == basic.iloc[i,0]:
            root_index = i

    # Select random interval
    interval = random.choice(intervals)
    # Find index of interval in the list of choices
    for j in range(6):
        if interval == intervals[j]:
            interval_index = j

    # Print quiz question
    print(f'\nThe root note is {root_note}. What is the {interval}?\n')

    # Accept user input
    x = input()

    # Define function that runs if the user's answer is incorrect
    def try_again():
        # Rerun quiz once the user corrects their answer
        x = input()
        if x == basic.iloc[root_index,interval_index+1]:
            print('\nCorrect.')
            quiz()
        # Allow user to stop quiz without correcting their answer
        elif x == 'stop':
            return
        # Rerun current function if the user answers incorrectly again
        else:
            print('\nTry again.\n')
            try_again()

    # Rerun quiz if the user is correct
    if x == basic.iloc[root_index,interval_index+1]:
        print('\nCorrect.')
        quiz()
    # Allow user to stop the quiz without answering
    elif x == 'stop':
        return
    # Run try_again function if the user answers incorrectly
    else:
        print('\nTry again.\n')
        try_again()

# Let user know how to end the quiz at the start
print(f'\nTYPE "stop" AT ANY TIME TO LEAVE THE QUIZ.')

# Initial run of function to start the quiz
quiz()