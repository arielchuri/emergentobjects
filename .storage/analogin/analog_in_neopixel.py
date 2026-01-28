# Emergent Objects
# Analogin input/output

import time
import board
import analogio
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1, auto_write=False)

analogin = analogio.AnalogIn(board.A1)

print("hello")

while True:
	print(analogin.value)

	if analogin.value > 600:
		print("hello")
		pixels[9] = (255, 50, 50)
	else:
		pixels[9] = (0, 0, 0)
	if analogin.value > 3200:
		pixels[8] = (255, 50, 50)
	else:
		pixels[8] = (0, 0, 0)
	if analogin.value > 4000:
		pixels[7] = (255, 50, 50)
	else:
		pixels[7] = (0, 0, 0)
	if analogin.value > 52000:
		pixels[6] = (255, 50, 50)
	else:
		pixels[6] = (0, 0, 0)
	if analogin.value > 60000:
		pixels[5] = (255, 50, 50)
	else:
		pixels[5] = (0, 0, 0)
	pixels.show()
	time.sleep(0.01)
