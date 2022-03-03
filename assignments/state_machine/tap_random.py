
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""This example prints to the serial console when the board is tapped."""
import time
# I needed cp from this library for the detect_taps.
# Because this library has neopixel built in I cannot import neopixel.
from adafruit_circuitplayground import cp
# import neopixel
import random
import board

# Change to 1 for single-tap detection.
# Change to 2 for double-tap detection.
cp.detect_taps = 1
x = random.randint(0,9)

while True:
	if cp.tapped:
		# print(random.randint( 0, 9))
		cp.pixels[x] = ( 0, 0, 0)
		oldx = x
		while oldx == x:
			x = random.randint(0,9)
		cp.pixels[x] = ( 90, 100, 80)
		cp.pixels.show()
	time.sleep(0.05)
