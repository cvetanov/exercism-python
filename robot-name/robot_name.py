import random
names = {}

def random_digit():
    return random.randint(0, 9)

def random_letter():
    return chr(random.randint(65, 65 + 25))

def generate_name():
    return '{}{}{}{}{}'.format(random_letter(), random_letter(), random_digit(), random_digit(), random_digit())

def name_exists(name):
    return name in names

def add_name(name):
    names[name] = True

class Robot(object):
    def __init__(self):
        self.reset()

    def reset(self):
        name = generate_name()
        while name_exists(name):
            name = generate_name()
        add_name(name)
        self.name = name

