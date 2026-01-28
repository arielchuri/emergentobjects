import time
import board
import digitalio
import neopixel

led = digitalio.DigitalInOut(board.D13)
led.switch_to_output()

buttonA = digitalio.DigitalInOut(board.BUTTON_A)
buttonA.switch_to_input(pull=digitalio.Pull.DOWN)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2, auto_write=False)

choicevar = 0
pink = ( 255, 80, 80)
pixels[choicevar] = pink
pixels.show()
apress = False

while True:
	if buttonA.value and apress == 0:  # button is pushed
		apress = True
		pixels[choicevar] = ( 0, 0, 0)
		print(choicevar)
		choicevar = choicevar + 1
		if choicevar > 9:
			choicevar = 0
		print(choicevar)
		pixels[choicevar] = pink
		pixels.show()
	elif buttonA.value == False:
		apress = False
	time.sleep(0.01)
