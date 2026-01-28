# Lecture: Electricity Fundamentals

**Week:** 3
**Date:** Feb 9
**Duration:** ~45 minutes

## Learning Outcomes

This lecture supports the following learning outcomes:

- **LO 2 - Tools, Materials, Methods:** Write and debug basic Python code and create electronic circuits using microprocessors.

## Overview

This lecture introduces the fundamental principles of electricity needed to design and build safe, functional electronic circuits. Students learn about voltage, current, resistance, and how to read circuit diagrams and calculate component values.

## Key Topics

### Basic Electrical Concepts

#### Voltage (V)
- Definition: electrical potential difference
- Measured in Volts (V)
- Analogy: water pressure in pipes
- Common voltages: 3.3V, 5V, 9V, 12V, 120V AC
- Importance in circuit design

#### Current (I)
- Definition: flow of electrical charge
- Measured in Amperes/Amps (A) or milliamps (mA)
- Analogy: water flow rate
- Direct current (DC) vs alternating current (AC)
- Current consumption in components

#### Resistance (R)
- Definition: opposition to current flow
- Measured in Ohms (Ω)
- Resistors and their purpose
- Variable resistance (potentiometers)
- Resistance in different materials

### Ohm's Law
- **V = I × R** (Voltage = Current × Resistance)
- Solving for different variables
- Practical calculations for circuit design
- Using Ohm's law to protect components
- Online calculators and tools

### Power
- **P = V × I** (Power = Voltage × Current)
- Measured in Watts (W)
- Heat generation in circuits
- Power ratings of components
- Battery capacity and power consumption

### Circuit Components

#### Essential Components
- **Resistors:** Limit current, divide voltage
- **LEDs:** Light emitting diodes, polarity matters
- **Switches:** Control circuit flow
- **Batteries:** Power sources
- **Wires:** Conductors
- **Breadboards:** Prototyping platforms

#### Component Properties
- Polarity (LEDs, electrolytic capacitors, diodes)
- Power ratings
- Tolerance
- Reading component values
- Datasheets and specifications

### Circuit Diagrams
- Schematic symbols for common components
- Reading and drawing schematics
- Following current flow
- Ground and power symbols
- Connection vs crossing wires
- Labeling conventions

### Series vs Parallel Circuits
- **Series:** Components in a line, current same, voltage divides
- **Parallel:** Components side-by-side, voltage same, current divides
- When to use each configuration
- Calculating total resistance
- LED arrays and resistor networks

### Safety

#### Safe Practices
- Low voltage DC is relatively safe (< 50V)
- Check polarity before powering
- Use appropriate wire gauges
- Fuses and circuit protection
- Heat sinks for high-power components

#### Common Hazards
- Short circuits
- Reverse polarity
- Exceeding component ratings
- Overheating
- Battery safety

## Practical Examples

### LED Circuit Design
- Calculating resistor value for LED
- Typical LED specifications (20mA, 2V forward voltage)
- Example calculation: 5V source, red LED
- (5V - 2V) / 0.020A = 150Ω resistor
- Choosing standard resistor values

### Button Input Circuit
- Pull-up vs pull-down resistors
- Debouncing concepts
- Reading digital input states
- Typical resistance values (10kΩ)

### Sensor Circuits
- Voltage dividers
- Reading analog values
- Variable resistance sensors
- Signal conditioning

## Key Questions

- Why do LEDs need current-limiting resistors?
- What happens if you exceed a component's rating?
- How do you calculate the right resistor value?
- When would you use series vs parallel?
- How do you read a circuit diagram?
- What's the difference between voltage and current?

## Activities

### In-Class Demonstrations
- Multimeter usage (measuring V, I, R)
- Building simple LED circuit on breadboard
- Showing series and parallel configurations
- Circuit troubleshooting demonstration
- Reading resistor color codes

### Hands-On Workshop
- Following lecture: Basic circuits workshop
- Students build their first circuits
- Practice with breadboards
- Use multimeters to measure values
- Troubleshoot common problems

## Calculations Students Should Master

1. Ohm's Law (V = I × R)
2. Power calculation (P = V × I)
3. LED resistor calculation
4. Series resistance (R_total = R1 + R2 + ...)
5. Parallel resistance (1/R_total = 1/R1 + 1/R2 + ...)
6. Voltage divider calculations

## Connections to Course

- Immediately applied in Circuit Prototyping Demo
- Practiced in Basic Circuits Workshop
- Circuit Plan assignment (due Week 4)
- Foundation for microcontroller integration
- Essential for Final Project
- Building on programming knowledge

## Resources

### Online Resources
- Electronics tutorials (SparkFun, Adafruit, Electronics Club)
- Ohm's law calculators
- Resistor color code calculators
- Circuit simulation tools (Tinkercad Circuits, Falstad)
- Component datasheets

### Tools
- Multimeters
- Breadboards
- Wire strippers
- Component kits
- Power supplies

### Course Materials
- electricity_intro directory
- Component reference guides
- Circuit examples
- Troubleshooting flowcharts

## Assessment

Students demonstrate understanding through:
- Circuit Plan assignment (due Week 4)
- Basic Circuits Workshop participation
- Successful circuit prototyping
- Proper component selection for projects
- Safe practices in lab work

## Tips for Teaching

- Use water/plumbing analogies consistently
- Do live calculations with real numbers
- Show real components while discussing them
- Demonstrate with multimeter measurements
- Build circuits in real-time
- Intentionally create errors and troubleshoot
- Emphasize safety without creating fear
- Connect to their Python programming knowledge
- Provide reference sheets and charts
- Make resources available for review
- Prepare for different math comfort levels
- Encourage questions and experimentation
- Link to previous knowledge (batteries, switches, light bulbs)
