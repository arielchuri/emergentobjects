import board
import analogio
import neopixel
import time

# Define colors
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

# Initialize potentiometer and NeoPixel
pot_pin = analogio.AnalogIn(board.A1)  # Replace A1 with the correct pin
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)  # Adjust the number of pixels if needed

while True:
    pot_value = pot_pin.value  # Read analog value
    if pot_value < 10922:  # 65535 / 6 (number of colors)
        pixels.fill(RED)
    elif 10922 <= pot_value < 21844:
        pixels.fill(YELLOW)
    elif 21844 <= pot_value < 32766:
        pixels.fill(GREEN)
    elif 32766 <= pot_value < 43688:
        pixels.fill(CYAN)
    elif 43688 <= pot_value < 54610:
        pixels.fill(BLUE)
    else:
        pixels.fill(PURPLE)
    pixels.show()
    time.sleep(0.05)


    