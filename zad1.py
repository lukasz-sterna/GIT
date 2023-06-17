# Napiszmy funkcję która przyjmować będzie stringa,
# następnie zliczy ilość samogłosek i zwróci ich sumę #


def vowel_counter(string):
    list_of_vowels = ["a", "ą", "e", "ę", "i", "o", "ó", "u", "y"]
    counter = 0

    for letter in string:
        if letter in list_of_vowels:
            counter += 1
    return counter
