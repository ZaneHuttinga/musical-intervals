# Import modules
import pandas as pd
import random

# Pull data from CSV file
complete = pd.read_csv('intervals.csv', usecols=[*range(8,21)])

# Create list of root notes from first column of pandas dataframe 'basic'
first = list(complete.iloc[0:21,0])

# Create list of modes
modes = list('Ionian', 'Dorian', 'Phrygian', 'Lydian', 'Mixolydian', 'Aeolian', 'Locrian')

# Define indices from the DataFrame 'complete' for each mode of the major scale.
# We will need these to determine whether the user's answers are correct.
# Note these don't necessarily equal the number of halfsteps from the root note
# because the augmented fourth and diminished fifth are both columns in the table.
ionian = [0, 2, 4, 5, 8, 10, 12]
dorian = [0, 2, 3, 5, 8, 10, 11]
phrygian = [0, 1, 3, 5, 8, 9, 11]
lydian = [0, 2, 4, 6, 8, 10, 12]
mixolydian = [0, 2, 4, 5, 8, 10, 11]
aeolian = [0, 2, 3, 5, 8, 9, 11]
locrian = [0, 1, 3, 5, 7, 9, 11]

mode_indices = list(ionian,dorian,phrygian,lydian,mixolydian,aeolian,locrian)

# Create list of key signatures
possible_signatures = ['0 sharps or flats',
                       '1 sharp', '2 sharps', '3 sharps', '4 sharps', '5 sharps', '6 sharps', '7 sharps',
                       '1 flat', '2 flats', '3 flats', '4 flats', '5 flats', '6 flats', '7 flats']

def quiz():
    # Select random key signature
    key_signature = random.choice(possible_signatures)

    # Select random mode
    mode = random.choice(modes)
    # Select the index of the mode
    mode_index = modes.index(mode)
    # Pick the corresponding list of indices from the list 'mode_indices'
    scale_indices = mode_indices[mode_index]

    # Find root note
    root = 

    # Find list of notes in the given key
    #scale = list(map(list(complete.iloc[root_index,:]).__getitem__, scale_indices))

    # Print quiz question
    print(f'\nKey signature: {key_signature}\nMode: {mode}\nWrite out the scale.\n')

    # Accept user input
    x = input()

    # Define function that runs if the user's answer is incorrect
    def try_again():
        # Rerun quiz once the user corrects their answer
        x = input()
        if x == complete.iloc[root_index,interval_index+1]:
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
    if x == complete.iloc[root_index,interval_index+1]:
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

# Let user know not to use double sharps or flats at the start
print(f'\nTYPE "DNE" IF THE REQUESTED KEY DOES NOT EXIST (without using double sharps or double flats).')

# Initial run of function to start the quiz
quiz()