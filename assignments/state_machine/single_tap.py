
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""This example prints to the serial console when the board is tapped."""
import time
# this library contains the tap functins.
from adafruit_circuitplayground import cp

# this sets the number of taps we are looking for by sending a number to *detect taps* in the cp library.
# Change to 1 for single-tap detection.
# Change to 2 for double-tap detection.
cp.detect_taps = 1
# this is just a value I created to count the number of taps.
tapnum = 0;

while True:
    # "tapped" is a function of the cp library. you could try print(cp.tapped) to see it.
    if cp.tapped:
		tapnum = tapnum + 1
		print(tapnum)
    time.sleep(0.05)
