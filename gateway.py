
import serial
import time

# Open COM ports for reading and writing
receive = serial.Serial('COM5', 9600)  # Adjust baud rate as per your device
send = serial.Serial('COM6', 9600)

binary_sequence = '10000011' + '01100001' + '01100111'+ '10000101'
bytes_to_send = bytes([int(binary_sequence[i:i+8], 2) for i in range(0, len(binary_sequence), 8)])
send.write(bytes_to_send)

while True:
    try:
        received_data = receive.read(4)
        # 4 byte gelmez ise blokluyor bekliyor
        for byte in received_data:
            byte_str = format(byte, '08b')  
            stop_bit = byte_str[-1]
            data_bits = byte_str[:-1]
            char = chr(int(data_bits, 2))
            output_string = f"Data Bits: {data_bits}, Stop Bit: {stop_bit}, Character: {char}\n"
            print(output_string.encode('ascii'))
            # TODO komut listesi ile karşılaştır. matchle istek at
    except Exception as e:
        print(e)
