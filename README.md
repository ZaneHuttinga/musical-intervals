# Quiz yourself on musical intervals

## Easier quiz (no sharps or flats)

The Python script 'basic.py' prompts the user with a random note (A, B, C, D, E, F or G) and a random interval (second, third, fourth, fifth, sixth or seventh) and asks "The root note is [note]. What is the [interval]?" The user must then give the note that is higher than the given note by the given interval. For example, G is a (perfect) fifth above C. The script would ask the user "The root note is C. What is the fifth?" and the user would answer "G". If the user answers correctly, the script will reply "Correct." and pose a new question of the same form. If the user answers incorrectly, the script will reply "Try again." and allow the user to answer the same question again. The user can end the quiz at any time by typing "stop".

## Harder quiz (including sharps and flats)

The Python script 'complete.py' uses the same format as 'basic.py' but allows sharps and flats, as well as major and minor seconds, thirds, sixths and sevenths; perfect and augmented fourths; and perfect and diminished fifths. It does not allow for double-sharped or double-flatted notes, though the CSV file can be modified to allow that.

## CSV file
Both Python scripts pull the random root notes and intervals from the file 'intervals.csv'. It also uses this file to grade the user's answers.