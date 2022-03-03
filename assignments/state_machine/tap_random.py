
import time
# I needed cp from this library for the detect_taps.
# Because this library has neopixel built in I cannot import neopixel.
# I must use cp.pixel from the cp library.
# import neopixel
from adafruit_circuitplayground import cp
import random
import board

# Change to 1 for single-tap detection.
# Change to 2 for double-tap detection.
cp.detect_taps = 1
# I removed the tapnum variable and now have a variable for which LED to light.
# We use the function "randint" in the library "random" to get a random number between 0 and 9.
x = random.randint(0,9)

while True:
	if cp.tapped:
		# print(random.randint( 0, 9))
		# Here we darken neopixel x by sending it the color black.
		cp.pixels[x] = ( 0, 0, 0)
		# We need to remember this number so we can darken it later so we save it in "oldx".
		oldx = x
		# We use a while loop to choose a random number.
		# The while loop keeps getting random numbers if oldx and x are the same.
		# The code would work ok if we only got the number once. Why do we put it in a loop?
		while oldx == x:
			x = random.randint(0,9)
		# When x and oldx are not equal, we light up that Neopixel.
		cp.pixels[x] = ( 90, 100, 80)
		cp.pixels.show()
		# No we go to the top and wait for a tap.
	time.sleep(0.05)
