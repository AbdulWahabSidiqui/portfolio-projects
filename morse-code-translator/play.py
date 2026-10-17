import winsound
import time




class MorsePlayer:
    DOT = 100
    DASH = 300
    FREQ = 700

    def play(self, morse):
        if "." not in morse and "-" not in morse:
            return
        for symbol in morse:
            if symbol == ".":
                winsound.Beep(self.FREQ, self.DOT)
            elif symbol == "-":
                winsound.Beep(self.FREQ, self.DASH)
            elif symbol == " ":
                time.sleep(0.3)
            elif symbol == "/":
                time.sleep(0.7)