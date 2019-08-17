alphabet_letters = [chr(i + 97) for i in range(26)]
print (alphabet_letters)

def is_pangram(sentence):
    lowercase_sentence = sentence.lower()
    for letter in alphabet_letters:
        if letter not in lowercase_sentence:
            return False
    return True
