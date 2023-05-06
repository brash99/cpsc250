def convert_int_to_binary(num):
    res = ""

    while num > 0:
        digit = num % 2
        # print(num, digit)
        res = str(digit) + res
        num = int(num / 2)

    return res


def convert_fraction_to_binary(num, p):
    count = 0
    res = ""

    while count < p:
        comparison = 2 ** (-1 - count)
        # print (num,comparison,res)
        if num >= comparison:
            res = res + "1"
            num = num - comparison
        else:
            res = res + "0"

        count = count + 1

    return res


def get_fp_binary_representation(n):
    # Take user input for the number of
    # decimal places user want result as
    # p = int(input("Enter the number of decimal places of the result : \n"))
    p = 48

    # Step 1:  split the number into two parts - both strings
    front, back = str(n).split('.')

    # Step 2:  convert the part in front of the decimal to binary
    if int(front) < 0:
        sign = "-"
        i_front = -int(front)
    else:
        sign = ""
        i_front = int(front)

    if i_front == 0:
        front_bin = "0"
    else:
        front_bin = convert_int_to_binary(i_front)

    # Step 3:  convert the part after the decimal to binary
    divisor = 10**len(back)
    back_bin = convert_fraction_to_binary(float(back)/divisor, p)

    # Step 4:  add the strings together and print the result
    bin_result = sign + front_bin + "." + back_bin
    print(bin_result)

    # Step 5:  Determine the exponent and mantissa
    if front_bin == "0":
        exponent = 0
        keep_going = True
        while keep_going:
            # print (back_bin[-exponent],exponent)
            if back_bin[-exponent] == "1":
                keep_going = False
                exponent = exponent + 1
            exponent = exponent - 1
        exponent = exponent - 1

        # print(exponent)
        back_bin = back_bin[-exponent:]
        mantissa_truncated = back_bin
    else:
        exponent = len(front_bin)-1
        mantissa = front_bin[1:] + back_bin
        mantissa_truncated = mantissa[0:23]

    true_result = sign + "1." + mantissa_truncated + " x 2^(" + str(exponent) + ")"
    print(true_result)

    # Step 6:  Convert to 32-bit floating point representation
    if int(front) < 0:
        bit1 = "1"
    else:
        bit1 = "0"

    exp = int(exponent)+127
    exp_binary_rep = convert_int_to_binary(exp)
    if len(exp_binary_rep) < 8:
        exp_binary_rep = "0" + exp_binary_rep

    if len(mantissa_truncated) < 23:
        mantissa_truncated = mantissa_truncated + (23-len(mantissa_truncated))*"0"

    if len(mantissa_truncated) > 23:
        mantissa_truncated = mantissa_truncated[0:23]

    res = bit1 + "|" + exp_binary_rep + "|" + mantissa_truncated
    return res


if __name__ == "__main__":

    fp_num = input("Enter your floating point value : \n")
    result = get_fp_binary_representation(fp_num)
    print(result)
