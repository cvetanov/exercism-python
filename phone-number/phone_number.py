import string

def invalid_number(number):
    return len(number) != 10 or number[0] in ['0', '1'] or number[3] in ['0', '1']

class Phone(object):
    def __init__(self, phone_number):
        no_punctuation = phone_number.translate(None, string.punctuation).replace(' ', '')
        number = no_punctuation if no_punctuation[0] != '1' else no_punctuation[1:]
        if invalid_number(number):
            raise ValueError('Invalid phone number')
        self.number = number
        self.area_code = number[:3]
    def pretty(self):
        return '({}) {}-{}'.format(self.area_code, self.number[3:6], self.number[6:])
