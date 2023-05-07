def swap_values(user_val1, user_val2, user_val3, user_val4):   
   temp = user_val1 
   user_val1 = user_val2
   user_val2 = temp
   
   temp = user_val3 
   user_val3 = user_val4
   user_val4 = temp
   
   return user_val1, user_val2, user_val3, user_val4

if __name__ == '__main__':   
   user_input1 = int(input())
   user_input2 = int(input())
   user_input3 = int(input())
   user_input4 = int(input())
   
   output1, output2, output3, output4 = swap_values(user_input1, user_input2, user_input3, user_input4)   
   print(f'{ str(output1) } { str(output2) } { str(output3) } { str(output4) }')
