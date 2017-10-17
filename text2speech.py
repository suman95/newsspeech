# Python code to convert text into speech
# Dependencies gtts and pygame

from gtts import gTTS
from pygame import mixer
import time


def text_to_speech(text):
	tts = gTTS(text=text, lang='en', slow=False)
	tts.save('test.mp3')
	mixer.init()
	mixer.music.load('test.mp3')
	mixer.music.play()
	while mixer.music.get_busy() == True:
		continue

# for testing purpose only
if __name__ == '__main__':
	text_to_speech("hello welcome to news anchor")