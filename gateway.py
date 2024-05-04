import serial
import time
# Open COM port
ser = serial.Serial('COM5', 9600)  # Adjust baud rate as per your device

while 1:
    try:
        received_data = ser.read(4)
        for byte in received_data:

            byte_str = format(byte, '08b')  # Convert to 8-bit binary string

            start_bit = byte_str[0]
            stop_bit = byte_str[-1]
            
            data_bits = byte_str[1:-1]

            char = chr(int(data_bits, 2))
            output_string = f"Start Bit: {start_bit}, Data Bits: {data_bits}, Stop Bit: {stop_bit}, Character: {char}\n"

            ser.write(output_string.encode('ascii'))
    except Exception as e:
        print(e)