from Crypto.Util.number import bytes_to_long, long_to_bytes

int_value = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
byte_data = long_to_bytes(int_value)
ascii_bytes=bytes(byte_data)
print(ascii_bytes.decode('utf-8'))
