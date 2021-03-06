import speech_recognition as sr
import difflib

commands = [
    "ВЛЕВО", "ВПРАВО",
    "ПУСК", "ОГОНЬ", "ПЛИ"
]

DIGITS_DICT = {48: None, 49: None, 50: None, 51: None, 52: None, 53: None, 54: None, 55: None, 56: None, 57: None}


class SpeechHandler:

    def __init__(self, turn_callback, fire_callback):
        self.turn_callback = turn_callback
        self.fire_callback = fire_callback

    def handle(self):
        r = sr.Recognizer()
        words = []

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Talk Now")
            data = r.record(source, duration=4)
            full_text = r.recognize_google(data, language='ru', show_all=True)
            for command in commands:
                similarities = []
                try:
                    for variant_src in full_text["alternative"]:
                        variant = variant_src["transcript"]
                        variant = variant.translate(DIGITS_DICT).strip()
                        similarities.append(
                            {"sim": SpeechHandler.similarity(variant, command.lower()), "transcript": variant_src["transcript"]})
                except TypeError:
                    fire()
                    return
                sim_index = SpeechHandler.find_max_index(similarities, lambda x: x["sim"])
                words.append(similarities[sim_index])

        command_index = SpeechHandler.find_max_index(words, key=lambda x: x["sim"])

        # Поворот
        if command_index < 2:
            split_transcript = words[command_index]["transcript"].split()
            argument = split_transcript[len(split_transcript) - 1]
            if command_index == 1:
                try:
                    self.turn_callback(int(argument))
                except ValueError:
                    print("FIRE!")
            else:
                try:
                    self.turn_callback(-int(argument))
                except ValueError:
                    print("FIRE!")

        # Пуск
        else:
            self.fire_callback()

    @staticmethod
    def similarity(s1, s2):
        normalized1 = s1.lower()
        normalized2 = s2.lower()
        matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
        return matcher.ratio()

    @staticmethod
    def find_max_index(sequence, key=lambda x: x):
        max_index = 0
        for i in range(len(sequence)):
            element = key(sequence[i])
            if element > key(sequence[max_index]):
                max_index = i
        return max_index


# Test
def fire():
    print("FIRE")


# Test
def turn(degree):
    if degree > 0:
        print(f"Turning {degree} degrees right")
    else:
        print(f"Turning {degree} degrees left")


if __name__ == '__main__':
    SH = SpeechHandler(turn, fire)
    input("WAITING KEYBOARD...")
    SH.handle()
