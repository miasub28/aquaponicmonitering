"""
This Raspberry Pi code was developed by newbiely.com
This Raspberry Pi code is made available for public use without any restriction
For comprehensive instructions and wiring diagrams, please visit:
https://newbiely.com/tutorials/raspberry-pi/raspberry-pi-lm35-temperature-sensor
"""


import Adafruit_ADS1x15
import time

# Create an ADC instance (ADS1015 or ADS1115)
adc = Adafruit_ADS1x15.ADS1115()

# Analog input channel connected to the LM35
analog_channel = 0

def read_lm35_temperature():
    # Read the raw ADC value
    raw_value = adc.read_adc(analog_channel, gain=1)

    # Convert the raw ADC value to millivolts
    millivolts = (raw_value * 4.096) / 32767.0 * 1000

    # Convert millivolts to Celsius using the LM35 formula
    temperature_celsius = millivolts / 10.0

    # Convert Celsius to Fahrenheit
    temperature_fahrenheit = (temperature_celsius * 9/5) + 32

    return temperature_celsius, temperature_fahrenheit

try:
    while True:
        celsius, fahrenheit = read_lm35_temperature()
        print(f'Temperature: {celsius:.2f}°C  ~  {fahrenheit:.2f}°F')
        time.sleep(1)

except KeyboardInterrupt:
    pass