import random

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 160)


def random_voice():
    voice = random.choice(voices)
    engine.setProperty('voice', voice.id)


words = []
fp = open('pte-words.txt', 'r', encoding='utf-8')
for line in fp:
    words.append(line.lower().strip())
fp.close()

fp = open('errors.txt', 'a', encoding='utf-8')
total = 0.0
correct = 0.0
buffer = None
try:
    word = random.choice(words)
    random_voice()
    while True:
        engine.say(word)
        engine.runAndWait()
        percent = correct / total * 100 if total > 0 else 0
        answer = input(f'[{int(total):-3d}:{percent:4.1f}%]> ').lower().strip()
        if answer == 'x':
            buffer = None
            print('             Cancelled.')
            continue

        total += 1
        if buffer:
            fp.write(buffer)
            fp.flush()
            buffer = None

        if answer != word:
            print(f'             {word}\n')
            buffer = f'{word}\n'

        else:
            correct += 1

        word = random.choice(words)
        random_voice()

except KeyboardInterrupt:
    print('\nBye.')
finally:
    fp.close()
