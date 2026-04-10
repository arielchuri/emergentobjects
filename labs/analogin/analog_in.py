# Emergent Objects
# Analogin input/output

import time
import board
import analogio

analogin = analogio.AnalogIn(board.A1)

print("hello")

while True:
	print(analogin.value)

	time.sleep(0.21)
