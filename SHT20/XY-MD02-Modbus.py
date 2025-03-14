# working code using modbus protocol for XY-MD02 device with SHT20 Temperature and Humidity sensor.
# install minimal modbus library -sudo pip3 install -U minimalmodbus

import minimalmodbus
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

serial_port = '/dev/ttyS0' #verify serial port 
slave_address = 1
baudrate = 9600

try:
    instrument = minimalmodbus.Instrument(serial_port, slave_address)
    instrument.serial.baudrate = baudrate
    instrument.serial.timeout = 2

    # Read input temperature (register 1)
    temperature_raw = instrument.read_register(1, 1, functioncode=4) #(register address, decimal point, function code)
    temperature = temperature_raw
    logging.info(f"Temperature: {temperature:.1f} °C")

    # Read input humidity (register 2)
    humidity_raw = instrument.read_register(2, 1, functioncode=4) #(register address, decimal point, function code)
    humidity = humidity_raw 
    logging.info(f"Humidity: {humidity:.1f} %")

except minimalmodbus.NoCommunicationError:
    logging.error("No communication with the instrument (no answer).")
except minimalmodbus.ModbusException as e:
    logging.error(f"Modbus error: {e}")
except Exception as e:
    logging.error(f"An unexpected error occurred: {e}")
