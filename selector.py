import random

activities = [
    'Read a book',
    'Play an instrument',
    'Call a friend',
    'Try origami',
    'Watch a movie',
    'Build a puzzle',
    'Write a short story',
    'Draw a cat',
    'Clean your room'
]

# random.randint(1, 5) --> random number between 1 and 5
# random.choice(array) --> random item in this array

selected = random.choice(activities) # randomly choose a friend

print('What should I do today?')
print(selected)
