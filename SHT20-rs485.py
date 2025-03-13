import serial
import time
import string

serial_port = '/dev/ttyS0'
baudrate = 9600
timeout = 1

ser = serial.Serial(serial_port, baudrate=baudrate, timeout=timeout)
time.sleep(2)

def capture_data():
    while True:
        if ser.in_waiting > 0:
            data = ser.read(ser.in_waiting)
            try:
                latin_data = data.decode('latin-1')
                printable_data = ''.join(filter(lambda x: x in string.printable, latin_data)).strip()
                if ',' in printable_data:
                    parts = printable_data.split(',')
                    temperature = parts[0].strip()
                    humidity = parts[1].strip()
                    print(f"Temperature: {temperature} °C")
                    print(f"Humidity: {humidity} %")
            except (UnicodeDecodeError, IndexError, ValueError) as e:
                print(f"Error parsing data: {e}")
        time.sleep(0.1)

capture_data()
ser.close()
