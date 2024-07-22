import pandas as pd
import random

basic = pd.read_csv('intervals.csv', usecols=[*range(0,7)])

first = list(basic.iloc[0:7,0])

intervals = ['second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

def quiz():
    root_note = random.choice(first)
    for i in range(7):
        if root_note == basic.iloc[i,0]:
            root_index = i

    interval = random.choice(intervals)
    for j in range(6):
        if interval == intervals[j]:
            interval_index = j

    print(f'\nThe root note is {root_note}. What is the {interval}?\n')

    x = input()

    def try_again():
        x = input()
        if x == basic.iloc[root_index,interval_index+1]:
            print('\nCorrect.')
            quiz()
        elif x == 'stop':
            return
        else:
            print('\nTry again.\n')
            try_again()

    if x == basic.iloc[root_index,interval_index+1]:
        print('\nCorrect.')
        quiz()
    elif x == 'stop':
        return
    else:
        print('\nTry again.\n')
        try_again()

print(f'\nTYPE "stop" AT ANY TIME TO LEAVE THE QUIZ.')

quiz()