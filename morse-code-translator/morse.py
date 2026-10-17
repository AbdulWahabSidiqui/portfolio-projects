from MorseCode import *

class MorseCodeConverter:
    def __init__(self):
        self.morse = MORSE_CODE
        self.reverse_morse = REVERSE_MORSE

    def morse_to_text(self,morse):
        result = ""
        words = morse.split()
        for word in words:
            if word == "/":
                result += " "
            elif word in self.reverse_morse:
                result += self.reverse_morse[word]
            else:
                return "Invalid Morse Code"
        return result.strip()

    def text_to_morse(self,text):
        result = ""
        for letter in text.upper():
            if letter not in self.morse:
                return "Invalid Input"

            result += self.morse[letter] + " "
        return result.strip()
