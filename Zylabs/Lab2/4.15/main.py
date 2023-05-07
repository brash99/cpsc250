highway_number = int(input())

# Output whether the highway is auxiliary (serving which primary), or primary
if ((highway_number < 1) or (highway_number > 999) or ((highway_number % 100) == 0)): # Invalid
    print(f'{highway_number} is not a valid interstate highway number.')
else: # Valid
    if (highway_number > 99):
        print(f'I-{highway_number} is auxiliary', end='')
        # Get the primary
        primary_number = highway_number % 100 # Gets the rightmost 2 digits
        print(f', serving I-{primary_number}', end='')
    else: # Must be 1-99
        primary_number = highway_number
        print(f'I-{primary_number} is primary', end='')
    # Ready now to output the direction. 
    if ((primary_number % 2) == 0): # Even
        print(', going east/west.')
    else: # Odd
        print(', going north/south.')
