# State Machine

Our object will likely have a variety of behaviors depending on the user's actions. Each set of behavior is a different *state* of our code.
In this lesson we will look at having different chunks of code running under different conditions.

The final code in this series runs throught the following states:

1. Wait for a hard tap. When tapped, light an led and darken the previous led.
   If LED 0 lights up, change to the second state.
1. Make LED 0 pink. 
1. If the user touch pad A6, move on to the fourth state.
1. Light up all of the Neopixels.
1. Wait for the user to touch A6 to start over.

```python
import time
# I needed cp from this library for the detect_taps.
# Because this library has neopixel built in I cannot import neopixel.
from adafruit_circuitplayground import cp
# import neopixel
import random
import board
# this library allows us to use one of the pads on the board as a touch sensor.
# Any piece of conductive material attached to this pad will also be a touch sensor.
import touchio

# We create a variable to use the touch sensor with pad A6.
touch_A6 = touchio.TouchIn(board.A6)

# Change to 1 for single-tap detection.
# Change to 2 for double-tap detection.
cp.detect_taps = 1
x = random.randint(0,9)
# we create a variable to keep track of the current "state" of our object.
state = 'begin'
print('begin')

while True:
	cp.pixels.fill(0)
	# Here we have a series of 'while' statements.
	# 'state' can only have one value at a time so only one will run at a time.
	while state == 'begin':
		# In which tapping chooses a neopixel to light up until it lights up pixel 0.
		if cp.tapped:
			# print(random.randint( 0, 9))
			cp.pixels[x] = ( 0, 0, 0)
			oldx = x
			while oldx == x:
				x = random.randint(0,9)
				print(x)
			cp.pixels[x] = ( 90, 100, 80)
			if x == 0:
				state = 'second'
	while state == 'second':
		# In which we light up the 0 pixel pink.
		cp.pixels[x] = ( 255, 40, 40)
		x = random.randint(0,1)
		print("third")
		state = 'third'
	while state == "third":
		# In which we wait for the user to touch the A6 pad.
		if touch_A6.value:
			print('touched')
			state = 'end'
	while state == "end":
		# In which we light the neopixels in very pretty colors.
		for i in range(5):
			# the for loop means we run this code 5 times and change the value of i each time.
			print('yellow')
			print(i)
			cp.pixels[i] = (80,80,0)
		for n in range(5, 10):
			print('blue')
			print(n)
			cp.pixels[n] = (5,5,255)
		time.sleep(1)
		state = 'wait'
	while state == "wait":
		# In which we wait for the user to touch the A6 pad.
		if touch_A6.value:
			print('touched')
			state = 'begin'
	time.sleep(0.05)
```
