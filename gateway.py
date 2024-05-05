import serial
import time

receive = serial.Serial('COM5', 9600)  
send = serial.Serial('COM6', 9600)

binary_sequence = '10000011' + '01100001' + '01100111' + '10000101'
bytes_to_send = bytes([int(binary_sequence[i:i+8], 2) for i in range(0, len(binary_sequence), 8)])
send.write(bytes_to_send)
received_chunk =b''
while True:
    try:
        received_data = receive.read(1)
        received_chunk+=received_data
        if len(received_chunk) >=4:
            for byte in received_chunk:
                byte_str = format(byte, '08b')  # Convert to 8-bit binary string
                stop_bit = byte_str[-1]
                received_chunk = byte_str[:-1]
                char = chr(int(received_chunk, 2))
                output_string = f"Data Bits: {received_chunk}, Stop Bit: {stop_bit}, Character: {char}"
                print(output_string.encode('ascii'))
            received_chunk =b''
        
    except Exception as e:
        print(e)
