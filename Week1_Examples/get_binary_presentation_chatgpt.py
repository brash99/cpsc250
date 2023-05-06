import struct

def float_to_binary(f):
    # Convert the floating-point number to its binary representation
    bits = struct.pack('>f', f)
    # Convert the binary representation to a string of 32 bits
    return ''.join(format(b, '08b') for b in bits)

# Example usage

n = float(input("Enter your floating point value : \n"))

binary_str = float_to_binary(n)
print(binary_str)