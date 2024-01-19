import pyttsx3


class PlayAudio:
    def __init__(self, voice='male', speakstatus=True):
        self.voice = 'male'
        self.speakStatus = speakstatus
        self.speakWords = {
            '0': 'zero',
            '1': 'one',
            '2': 'two',
            '3': 'three',
            '4': 'four',
            '5': 'five',
            '6': 'six',
            '7': 'seven',
            '8': 'eight',
            '9': 'nine',
            '+': 'plus',
            '-': 'minus',
            '*': 'times',
            '/': 'divided by',
            'sqrt': 'square root',
            'power': 'power',
            '=': 'equals',
            '.': 'dot',
            ',': 'comma',
            'Sin': 'Sine',
            'Cos': 'Cosine',
            'Tan': 'Tan',
            '^': 'Power',
            'toRad': 'To Radian',
            'toDeg': 'To Degree'

        }
        self.engine = pyttsx3.init()
        v = self.engine.getProperty('voices')
        self.engine.setProperty('voice', v[0].id)
        print(v)

    def speak(self, content):
        if self.speakStatus == True:
            self.engine.say(self.speakWords[content])
            self.engine.runAndWait()


if __name__ == '__main__':
    ob = PlayAudio()
    ob.speak('1')
