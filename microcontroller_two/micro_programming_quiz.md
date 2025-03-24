# Micro Programming Quiz

## Starter Code

```python
import board
import digitalio
import analogio
import pwmio
import time


# Setup the pins for the pot, leds and buttons.
led1 = digitalio.DigitalInOut(board.GP14)
led1.direction = digitalio.Direction.OUTPUT
led2 = pwmio.PWMOut(board.GP15, frequency=1000)

button1 = digitalio.DigitalInOut(board.GP13)
button1.switch_to_input(pull=digitalio.Pull.DOWN)

potentiometer = analogio.AnalogIn(board.GP26)
ldr = analogio.AnalogIn(board.GP27)

# Create the variables

previousButton1State = button1.value

# This is the variable that will change when we press the button.
myMode1 = False

while True:
    currentButton1State = button1.value
    if currentButton1State != previousButton1State:
        # print statements like these can be seen in the serial terminal
        # print('yes')
        if not currentButton1State:
            myMode1 = not myMode1
            print('myMode1 =', myMode1)
            print("ldr.value")
        else:
            print("down")
    previousButton1State = currentButton1State
    led1.value = myMode1
    # print("led1 = ", led1.value)
    # This line sets the PWM (pulse width modulation) to the potentiometer value.
    led2.duty_cycle = potentiometer.value
```

## Links

- [Python 1](../programming_intro/python_lesson.md)
- [Python 2](../programming_2/programming_02.md)
- [Microcontroller 1](../microcontroller_intro/microcontroller_intro.md)
- [Microcontroller 2](../microcontroller_two/)

## Problem One

An LED gets brighter as the room gets darker.

## Problem Two

Make an LED slowly fade in and out.

## Problem Three

An LED turns on when the room get dark. The level of darkness required to turn on the LED may be adjusted with a potentiometer.

## Problem four

On button press, an off LED becomes brighter in 6 steps. Each step being 3/4 of a second long.
The button will turn off the LED at any time.

## Problem five

Two buttons. Pressing button1 changes the effect of Button2. Button2 will either, make an LED blink, or make the same LED 60% bright, or make the LED turn off.
(use touch sensor for the second button)
