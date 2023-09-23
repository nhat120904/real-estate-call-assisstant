# from pywinauto.application import Application
# from timeit import default_timer as timer
# from collections import deque
from chat import call_assisstant

# import numpy as np
# import pyaudio
# import torch, torchaudio
# import soundfile as sf
# import threading, queue, os, time


import asyncio #, websockets
from websockets.server import serve

class WatchedValue:
	def __init__(self, value):
		self._value = value
		self._changed = False

	@property
	def value(self):
		return self._value
	
	@value.setter
	def value(self, new_value):
		self._value = new_value
		self._changed = True

	def has_changed(self):
		if self._changed:
			self._changed = False
			return True
		return False

# def int16_to_float32(x):
# 	abs_max = np.abs(x).max()
# 	x = x.astype('float32')
# 	if abs_max > 0:
# 		x *= 1 / 32768
# 	x = x.squeeze()
# 	return x

# def load_whisper(q):
# 	app = Application().start("./WhisperDesktop.exe")
# 	initial_window = app.window(title="Transcribe Audio File")
# 	initial_window.wait('visible', timeout=10)
# 	q.put((initial_window, app))

# def preprocess():
# 	temp = "./temp"
# 	if os.path.exists(temp):
# 		for f in os.listdir(temp):
# 			os.remove(os.path.join(temp, f))
# 	else:
# 		os.mkdir(temp)


# def remove_bom(utf8_with_bom):
# 	bom = b'\xEF\xBB\xBF'
# 	if utf8_with_bom.startswith(bom):
# 		return utf8_with_bom[len(bom):].decode('utf-8')
# 	return utf8_with_bom.decode('utf-8')

current_res = WatchedValue("")
utf8 = WatchedValue("")

def main():
	global current_res, utf8
	print("Starting")
	while True:
		# preprocess()
		# start_time = timer()
		# while True:
		# 	data = torch.from_numpy(int16_to_float32(np.frombuffer(stream.read(CHUNK), dtype=np.int16)))
		# 	confidences = model(data, RATE).item()
		# 	if confidences > 0.5:
		# 		frames.append(data)
		# 		print("too high, capture")
		# 		current_res.value = "too high, capture"
		# 		start_time = timer()
		# 	else:
		# 		print("too low, skip")
		# 		current_res.value = "too low, skip"
		# 		if timer() - start_time >= STOP_THRESHOLD and len(frames) != 0:
		# 			print("stop!")
		# 			current_res.value = "stop!"
		# 			break

		# result = torch.cat(list(frames))
		# sf.write('./temp/out.wav', result.numpy(), RATE)
		# frames.clear()
		# # wp.print_control_identifiers()
		# wp.Edit.set_text("./temp/out.wav")
		# wp.Edit2.set_text("./temp/out.txt")
		# wp.TranscribeButton.click()
		# current_res.value = "transcribing"
		
		# cw = pre_wp.window(title="Transcribe Completed")
		# cw.wait('visible', timeout=100)

		# cw.OKButton.click()
		# current_res.value = "done"
		# with open("./temp/out.txt", "rb") as f:
		# 	utf8_with_bom = f.read()
		# utf8 = remove_bom(utf8_with_bom)
		# utf8 = utf8.strip()
		# if len(utf8) > 0:
		# print(utf8)
		# current_res.value = "[user]" + utf8
		# current_res.value = utf8

		# time.sleep(10)
		# analyze = call_assisstant(utf8, current_res)
		# if analyze == 1:
		# 	break
		# else:
		# 	continue
		# break

		if utf8.has_changed():
			current_res.value = "[user]" + utf8.value
			analyze = call_assisstant(utf8.value, current_res)
			if analyze == 1:
				reset_con(current_res)
	# wp.CloseButton.click()

async def send_message(websocket):
	global current_res
	while True:
		if current_res.has_changed():
			await websocket.send(current_res.value)
		else:
			await asyncio.sleep(1/30)

async def get_message(websocket):
	global utf8
	while True:
		utf8.value = await websocket.recv()
		utf8.value = utf8.value.strip()
		print(utf8.value)
		await asyncio.sleep(1/30)

# import websockets.client

# async def server():
# 	async with websockets.client.connect("ws://localhost:8765") as websocket:
# 		send = asyncio.create_task(send_message(websocket))
# 		get = asyncio.create_task(get_message(websocket))
# 		await asyncio.gather(send, get)

def reset_con(current_res):
	reset_string = """address: null
price: null
property_type: null
area: null
bedrooms: null
bathrooms: null
house_direction: null
description: null
floors: null
installment_payment: null
furniture: null
balcony_direction: null"""

	with open("current_prompt.txt", "w") as f:
		f.write(reset_string)
		current_res.value = "[pr]\n" + reset_string

if __name__ == '__main__':
	# q = queue.Queue()
	# wp = threading.Thread(target=load_whisper, args=(q,))
	# wp.start()
	# model, _ = torch.hub.load(repo_or_dir='snakers4/silero-vad', model='silero_vad', force_reload=True, onnx=True)

	# FORMAT = pyaudio.paInt16
	# CHANNELS = 1
	# RATE = 16000
	# NUM = 10
	# CHUNK = int(RATE / NUM)
	# STOP_THRESHOLD = 1

	# frames = deque()
	# audio = pyaudio.PyAudio()
	# stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
	
	# wp.join()
	# (wp, pre_wp) = q.get()

	send_server = serve(send_message, "localhost", 8765)
	get_server = serve(get_message, "localhost", 8766)

	reset_con(current_res)
	# asyncio.get_event_loop().run_until_complete(asyncio.gather(send_server, get_server))
	asyncio.get_event_loop().run_until_complete(send_server)
	asyncio.get_event_loop().run_until_complete(get_server)
	asyncio.get_event_loop().run_in_executor(None, main)
	asyncio.get_event_loop().run_forever()