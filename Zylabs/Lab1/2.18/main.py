nickels = int(input())
dimes = int(input())
quarters = int(input())
dollars = (quarters*25 + dimes*10 + nickels*5) / 100.0
print(f'Amount: ${dollars:.2f}')
