
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""This example prints to the serial console when the board is tapped."""
import time
from adafruit_circuitplayground import cp

# Change to 1 for single-tap detection.
# Change to 2 for double-tap detection.
cp.detect_taps = 1
tapnum = 0;

while True:
    if cp.tapped:
		tapnum = tapnum + 1
		print(tapnum)
    time.sleep(0.05)
