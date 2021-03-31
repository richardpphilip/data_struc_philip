import random


sweepstakes_contestants = {
    # keys will be fname lname ticket#

    1: 'rich philip',
    2: 'regina wang',
    3: 'laura philip',
    4: 'richard philip',
    5: 'alison philip'
}

print(sweepstakes_contestants[random.randint(0, 4)])