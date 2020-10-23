import random

def main(x):
    original = "hallo"
    second = "gedag"
    third = "groeten"
    randomised1 = ''.join(random.sample(original, len(original)))
    randomised2 = ''.join(random.sample(second, len(second)))
    randomised3 = ''.join(random.sample(third, len(third)))
    print(randomised1)
    print(randomised2)
    print(randomised3)
    return main(x)

