# In this program, the struct module is used to convert the floating-point number
# to its binary representation. The pack function takes two arguments: a format
# string that specifies the desired byte order (>, for big-endian), and the
# floating-point number f. The result is a bytes object that represents the
# binary value of the floating-point number.

# The format function is used to convert each byte of the binary representation
# to an 8-bit binary string ('08b' specifies a zero-padded 8-bit binary string).
# The resulting strings are concatenated to form a 32-bit binary string, which
# is returned as the output of the function.

# Note that this implementation assumes that the floating-point number is
# represented using the IEEE 754 single-precision format (32 bits). If the input
# number is outside the range representable by this format (i.e., too large
# or too small), the output may not be accurate.


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
