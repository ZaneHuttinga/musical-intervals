import pandas as pd
import random

complete = pd.read_csv('intervals.csv', usecols=[*range(8,21)])

first = list(complete.iloc[0:21,0])

intervals = ['minor second', 'major second', 'minor third', 'major third', 'perfect fourth', 'augmented fourth', 'diminished fifth', 'perfect fifth', 'minor sixth', 'major sixth', 'minor seventh', 'major seventh']

def quiz():
    root_note = random.choice(first)
    for i in range(21):
        if root_note == complete.iloc[i,0]:
            root_index = i

    interval = random.choice(intervals)
    for j in range(12):
        if interval == intervals[j]:
            interval_index = j

    print(f'\nThe root note is {root_note}. What is the {interval}?\n')

    x = input()

    def try_again():
        x = input()
        if x == complete.iloc[root_index,interval_index+1]:
            print('\nCorrect.')
            quiz()
        elif x == 'stop':
            return
        else:
            print('\nTry again.\n')
            try_again()

    if x == complete.iloc[root_index,interval_index+1]:
        print('\nCorrect.')
        quiz()
    elif x == 'stop':
        return
    else:
        print('\nTry again.\n')
        try_again()

print(f'\nTYPE "stop" AT ANY TIME TO LEAVE THE QUIZ.')

print(f'\nTYPE "DNE" IF THE REQUESTED NOTE DOES NOT EXIST (without using double sharps or double flats).')

quiz()