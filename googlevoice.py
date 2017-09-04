import threading
import os.path
import hashlib
from gtts import gTTS

import gst
import time

class GoogleVoice:
	def speak(self, text):
		t = threading.Thread(target=self.speakThread, args=(text, ))
		t.start()

	def speakThread(self, text):
		m = hashlib.md5()
		m.update(text)

		filename = m.hexdigest() + ".mpga"
		filepath = os.path.abspath(filename)
		if not os.path.isfile(filepath):
			self.downloadGoogleVoice(text, filepath)
		print(filepath)

		pl = gst.element_factory_make("playbin", "player")
		pl.set_property('uri','file://' + filepath)
		pl.set_state(gst.STATE_PLAYING)
		time.sleep(3)

	def downloadGoogleVoice(self, text, filepath):
		tts = gTTS(text=text, lang='sv')
		tts.save(filepath)

