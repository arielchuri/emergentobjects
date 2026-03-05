# Basic Circuits Lab

**Related Lecture:** Electricity Fundamentals

## Overview
This hands-on lab introduces fundamental electrical concepts through building and measuring simple circuits. You'll learn to use a breadboard, calculate resistor values, measure voltage and current, and understand the difference between series and parallel circuits.

## Learning Objectives
- Build circuits on a breadboard using proper technique
- Calculate resistor values using Ohm's Law
- Measure voltage, current, and resistance with a multimeter
- Understand series and parallel circuit behavior
- Read circuit diagrams and implement them physically
- Troubleshoot common circuit problems

## Materials Required
From your kit:
- Raspberry Pi Pico (for 3.3V power only - no programming needed)
- USB cable to power the Pico
- Breadboard
- Jumper wires (various lengths)
- Multimeter
- LEDs (at least 3)
- Resistors: 220Ω (or 100-220Ω range), 1kΩ, 10kΩ (or 1MΩ if needed)
- Button/pushbutton
- Potentiometer
- Light dependent resistor (LDR/photoresistor)

## Safety Notes
- We're working with low voltage (3.3V) which is very safe
- Always check polarity before powering your circuit
- If any component gets hot, disconnect power immediately
- Never short circuit power to ground directly

## Resources

[Pico Pin-out Diagram](https://github.com/arielchuri/emergentobjects/blob/main/parts/microcontroller_intro/raspberry_pi_Pico-R3-Pinout-narrow.png)

## Background: Breadboard Basics

Before starting, understand how your breadboard works:
- **Power rails** (the long vertical columns on each side): All holes in a rail are connected
- **Component rows** (the numbered horizontal rows in the center): Holes in each row segment are connected horizontally (usually 5 holes per segment)
- **Center gap**: The two sides are NOT connected across the center gap

**Convention:**
- Use the left or right power rail for positive voltage (Red line. Use red wire)
- Use the opposite rail for ground/GND (Blue line. Use black wire)

## Part 1: Setting Up Power

Before building circuits, set up your power supply.

### Steps:
1. Connect your Raspberry Pi Pico to your computer via USB
2. Use a red jumper wire to connect pin 36 (3V3 OUT) on the Pico to the positive (+) power rail on your breadboard
3. Use a black jumper wire to connect any GND pin on the Pico (pin 3, 8, 13, 18, 23, 28, 33, or 38) to the negative (-) power rail

**Note:** We're using the Pico only as a power source in this lab. No programming required.

### Verify with Multimeter:
4. Set your multimeter to DC voltage mode (V with straight/dashed line, usually 20V range)
5. Touch the black probe to ground rail, red probe to positive rail
6. You should read approximately 3.3V

**Checkpoint:** Show your instructor the voltage reading before proceeding.

---

## Part 2: Simple LED Circuit

Build the most basic LED circuit to understand polarity and current limiting.

### Theory:
- LEDs have polarity: long leg = anode (+), short leg = cathode (-)
- LEDs need current-limiting resistors to prevent burnout
- Using Ohm's Law: R = (V_source - V_LED) / I_desired
- For red LED: V_LED ≈ 2V, I_desired = 20mA = 0.020A
- Calculation: R = (3.3V - 2V) / 0.020A = 65Ω
- Since we don't have 65Ω, use 220Ω (safer - slightly less current)

### Circuit Diagram:
```
3.3V ---[220Ω]---[LED>]--- GND
         (resistor) (long leg to resistor)
```

### Steps:
1. Insert a 220Ω resistor into the breadboard: one leg in the + power rail, other leg in a component row (e.g., row 10)
2. Insert LED long leg in the same row as the resistor (row 10), short leg in a different row (e.g., row 12)
3. Use a jumper wire from the LED short leg row to the ground rail

### Measurements:
4. **Measure voltage across LED:** Touch multimeter probes to each LED leg. What voltage do you read? _______V
5. **Measure voltage across resistor:** Probes on each resistor leg. What voltage? _______V
6. **Question:** Do the two voltages add up to approximately 3.3V? Why?

### Calculating Actual Current:
7. Using the voltage you measured across the resistor and Ohm's Law (I = V/R):
   - V_resistor = _______V
   - R = 220Ω
   - I = _______mA

**Checkpoint:** Verify your LED lights up and record your measurements.

---

## Part 3: Series vs Parallel Circuits

Build both configurations to see the difference in behavior.

### Part 3A: LEDs in Series

**Theory:** In series, current is the same through all components, but voltage divides.

### Circuit Diagram:
```
3.3V ---[220Ω]---[LED1>]---[LED2>]--- GND
```

### Steps:
1. Keep your 220Ω resistor connected to + rail
2. Connect LED1 long leg to resistor, short leg to a new row
3. Connect LED2 long leg to LED1 short leg row, LED2 short leg to GND

### Observations:
- Do the LEDs light? _______
- Are they bright or dim? _______
- Measure voltage across each LED: LED1 = _______V, LED2 = _______V
- **Question:** Why might the LEDs be dim or not light at all?
- **Answer:** With two ~2V LEDs (4V total needed) but only 3.3V supply, there's insufficient voltage.

### Part 3B: LEDs in Parallel

**Theory:** In parallel, voltage is the same across all components, but current divides.

### Circuit Diagram:
```
         +--- [220Ω]---[LED1>]--- GND
3.3V ---|
         +--- [220Ω]---[LED2>]--- GND
```

**Important:** Each LED needs its own resistor in parallel!

### Steps:
1. Disconnect the series circuit
2. Build two identical LED circuits side by side:
   - Circuit 1: + rail → 220Ω resistor → LED1 → GND rail
   - Circuit 2: + rail → 220Ω resistor → LED2 → GND rail

### Observations:
- Do the LEDs light? _______
- Are they brighter than in series? _______
- Measure voltage across each LED: LED1 = _______V, LED2 = _______V
- **Question:** What happens if you disconnect one LED? Does the other stay lit?

**Checkpoint:** Demonstrate both series and parallel configurations to your instructor.

---

## Part 4: Button Input Circuit with Pull-Down Resistor

Learn how buttons work in digital circuits.

### Theory:
- Buttons/switches mechanically connect two points
- Digital inputs need defined states: HIGH (3.3V) or LOW (0V)
- Pull-down resistor keeps input LOW when button is not pressed
- When pressed, input goes HIGH

### Circuit Diagram:
```
3.3V ----+
         |
      [Button]
         |
         +---- Output point (measure here)
         |
       [10kΩ]
         |
        GND
```

### Steps:
1. Insert your button into the breadboard spanning the center gap
2. Connect one side of the button to + rail with a jumper wire
3. Connect the other side of the button to a resistor (use 1kΩ or 1MΩ if no 10kΩ)
4. Connect the other end of the resistor to GND rail
5. The point between the button and resistor is your "output"

### Measurements:
6. Set multimeter to DC voltage
7. Measure voltage at the output point (between button and resistor) to GND:
   - Button NOT pressed: _______V (should be ~0V)
   - Button pressed: _______V (should be ~3.3V)

### Understanding:
- **Question:** Why do we need the resistor? What would happen without it?
- **Answer:** Without the resistor, pressing the button would short 3.3V directly to GND (bad!). The resistor limits current and defines the LOW state.

**Checkpoint:** Demonstrate button operation with multimeter readings.

---

## Part 5: Potentiometer as Voltage Divider

Explore variable resistance and voltage division.

### Theory:
- Potentiometers are variable resistors with three pins
- Center pin is the wiper; outer pins are ends of resistive element
- Turning the knob changes the resistance ratio
- Creates an adjustable voltage divider

### Circuit Diagram:
```
3.3V ---- Pin 1 (outer)

          Pin 2 (center/wiper) ---- Output (measure here)

GND ----- Pin 3 (outer)
```

### Steps:
1. Insert potentiometer into breadboard
2. Connect one outer pin to + rail
3. Connect other outer pin to GND rail
4. The center pin is your voltage output

### Measurements:
5. Measure voltage at center pin to GND while turning the knob:
   - Fully counterclockwise: _______V
   - Middle position: _______V
   - Fully clockwise: _______V

### Add an LED:
6. Connect the center pin → 220Ω resistor → LED → GND
7. Turn the potentiometer and observe the LED brightness change

### Understanding:
- **Question:** What's the voltage range you can create? _______V to _______V
- **Formula:** V_out = V_in × (R_bottom / R_total)

**Checkpoint:** Demonstrate LED brightness control with potentiometer.

---

## Part 6: Light Sensor Circuit

Build a sensor circuit using a photoresistor (light dependent resistor).

### Theory:
- Photoresistors change resistance based on light: bright = low resistance, dark = high resistance
- Combine with fixed resistor to create voltage divider
- Voltage changes with light level

### Circuit Diagram:
```
3.3V ---- [Photoresistor]
                |
                +---- Output (measure here)
                |
             [1kΩ]
                |
              GND
```

### Steps:
1. Connect photoresistor between + rail and a component row
2. Connect 1kΩ resistor from that same row to GND rail
3. The point between them is your output

### Measurements:
4. Measure output voltage in different light conditions:
   - Bright light (flashlight or window): _______V
   - Normal room light: _______V
   - Covered/dark (hand over sensor): _______V

### Add LED Indicator:
5. Connect output point → LED (long leg here, watch polarity!) → GND
6. Observe: LED brightness changes with light level!

### Understanding:
- **Question:** Why does voltage go UP when light is blocked?
- **Answer:** In darkness, photoresistor resistance increases dramatically. Since it's on top of the voltage divider, higher resistance means more voltage drops across it, leaving less at the output. (Wait, let me reconsider the circuit...)
- **Correction:** With photoresistor on top and fixed resistor on bottom, when photoresistor resistance increases (dark), the output voltage DECREASES because less current flows, and less voltage drops across the bottom resistor.

**Checkpoint:** Show voltage changing with light level.

---

## Part 7: Multimeter Practice

Practice all three multimeter modes.

### Voltage Measurement:
- Already practiced above
- Multimeter in parallel with component
- Set to DC V, appropriate range

### Resistance Measurement:
1. **Disconnect power from breadboard** (unplug Pico USB)
2. Set multimeter to resistance mode (Ω)
3. Measure your resistors:
   - Resistor labeled 220Ω: Actual = _______Ω
   - Resistor labeled 1kΩ: Actual = _______Ω
4. Measure photoresistor in bright light: _______Ω
5. Measure photoresistor in darkness: _______Ω
6. Measure potentiometer resistance:
   - Between outer pins (total resistance): _______Ω
   - Turn knob and measure between center and each outer pin

### Current Measurement (Advanced):
**Warning:** Current measurement requires breaking the circuit and inserting the multimeter in series.

1. Build simple LED circuit: 3.3V → 220Ω → LED → (break here) → GND
2. Set multimeter to DC current mode (A or mA)
3. Connect multimeter probes across the break point (in series)
4. Read current: _______mA
5. Does this match your calculation from Part 2? _______

**Important:** Return multimeter to voltage mode when done!

---

## Challenges (Optional Advanced Work)

### Challenge 1: LED Brightness Levels
Create a circuit with three LEDs that light at different brightness levels using only different resistor values. Calculate the resistor needed for:
- Full brightness (20mA): _______Ω
- Half brightness (10mA): _______Ω
- Quarter brightness (5mA): _______Ω

### Challenge 2: Light-Activated LED
Create a circuit where an LED turns on only when it's dark. You'll need to use the photoresistor circuit and think about the voltage divider configuration.

### Challenge 3: Resistance Calculator
Without using the resistor color code, determine the value of an unknown resistor by:
1. Building a voltage divider with the unknown resistor and a known resistor
2. Measuring the output voltage
3. Calculating the unknown resistance using the voltage divider formula

---

## Troubleshooting Guide

### LED doesn't light:
- [ ] Check LED polarity (long leg to +)
- [ ] Check power connections (Pico powered on?)
- [ ] Measure voltage across LED (should be 1.5-3V)
- [ ] Check breadboard connections (components in same row?)
- [ ] Verify resistor is working (measure it)

### Button doesn't change voltage:
- [ ] Check button is across center gap
- [ ] Verify power and ground connections
- [ ] Make sure measuring at correct point
- [ ] Button might need firm press

### Multimeter reads 0 or weird values:
- [ ] Check mode (voltage vs resistance vs current)
- [ ] Check probe connections
- [ ] For resistance: power must be OFF
- [ ] For current: must be in series
- [ ] Check battery in multimeter

### Potentiometer doesn't work:
- [ ] Verify three pins: outer-to-outer should show full resistance
- [ ] Center pin should be connected
- [ ] Turn knob through full range

---

## Completion Criteria

Complete the following to finish this lab:

- [ ] Successfully powered breadboard from Raspberry Pi Pico
- [ ] Built and measured simple LED circuit
- [ ] Demonstrated series LED circuit behavior
- [ ] Demonstrated parallel LED circuit behavior
- [ ] Built button circuit with pull-down resistor
- [ ] Used potentiometer as voltage divider to control LED
- [ ] Built light sensor circuit and observed voltage changes
- [ ] Measured voltage, resistance, and current with multimeter
- [ ] Recorded all measurement values in this document
- [ ] Answered all understanding questions

---

## Reflection Questions

Answer these after completing the lab:

1. **Ohm's Law Application:** Describe a situation in this lab where you used Ohm's Law to calculate a value. What were you trying to find?

2. **Series vs Parallel:** In your own words, explain the key difference between series and parallel circuits. When would you use each?

3. **Voltage Dividers:** Why are voltage dividers useful? Give an example from this lab.

4. **Troubleshooting:** What problem did you encounter during this lab and how did you solve it?

5. **Real-World Application:** Describe a device or object in your daily life that might use one of the circuits you built today.

---

## Additional Resources

### Online Calculators:
- [Ohm's Law Calculator](https://www.calculator.net/ohms-law-calculator.html)
- [LED Resistor Calculator](https://www.digikey.com/en/resources/conversion-calculators/conversion-calculator-led-series-resistor)
- [Voltage Divider Calculator](https://www.digikey.com/en/resources/conversion-calculators/conversion-calculator-voltage-divider)

### Circuit Simulators:
- [Tinkercad Circuits](https://www.tinkercad.com/circuits) - Visual breadboard simulator
- [Falstad Circuit Simulator](https://www.falstad.com/circuit/) - Interactive circuit behavior

### Reference Materials:
- [SparkFun: How to Use a Breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)
- [SparkFun: How to Use a Multimeter](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter)
- [Resistor Color Code Chart](https://www.digikey.com/en/resources/conversion-calculators/conversion-calculator-resistor-color-code)

### Component Datasheets:
- Check component values and specifications
- Learn maximum ratings and typical operating conditions
- Available from Adafruit, SparkFun, or manufacturer websites

---

**Remember:** The goal is understanding, not perfection. Circuits might not work the first time - troubleshooting is part of learning! Ask questions and experiment safely.
