import time
import board
import pwmio
from analogio import AnalogOut

pwm1 = pwmio.PWMOut(board.LED, frequency=5000, duty_cycle=0)
piezo = pwmio.PWMOut(board.A2, duty_cycle=0, frequency=440, variable_frequency=True)
analog_out = AnalogOut(board.A0)

while True:
    # PWM
    for i in range(100):
        # PWM LED up and down
        if i < 50:
            pwm1.duty_cycle = int(i * 2 * 65535 / 100)  # Up
        else:
            pwm1.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
        time.sleep(0.01)

    # PWM Piezo Tones
    for f in (262, 294, 330, 349, 392, 440, 494, 523):
        piezo.frequency = f
        piezo.duty_cycle = 65535 // 2  # On 50%
        time.sleep(0.25)  # On for 1/4 second
        piezo.duty_cycle = 0  # Off
        time.sleep(0.05)  # Pause between notes
    time.sleep(0.5)

    # True Analog Out
    for i in range(0, 65535, 64):
        analog_out.value = i
