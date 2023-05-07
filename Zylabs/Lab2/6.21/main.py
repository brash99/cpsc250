def int_to_reverse_binary(num1):
    binary_val = ''

    while num1 > 0:
        if (num1 % 2) == 0:
            binary_val += '0'
        else:
            binary_val += '1'
        num1 = num1 // 2

    return binary_val;


def string_reverse(input_string): 
    reverse_input = ''
    
    for i in range(len(input_string)-1, -1, -1): 
        reverse_input += input_string[i]
    
    return reverse_input

if __name__ == '__main__':
    user_input = int(input())
    
    binary_string = str(int_to_reverse_binary(user_input))
    binary_string = str(string_reverse(binary_string))
    
    print(binary_string)
