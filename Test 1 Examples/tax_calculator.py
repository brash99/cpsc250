# Zybooks 22.13

TEN_PCT = 0.1
TWELVE_PCT = 0.12
TWENTY_TWO_PCT = 0.22
TWENTY_FOUR_PCT = 0.24

# Calculate AGI and repair any negative values
def calc_AGI(wages, interest, unemployment):
    agi = abs(wages) + abs(interest) + abs(unemployment)
    return agi

# Calculate deduction depending on single, dependent or married
def get_deduction(status):
    deduction = 0

    if status == 2:
        deduction = 24000
    elif status == 1:
        deduction = 12000
    else:
        deduction = 6000

    return deduction

# Calculate taxable but not allow negative results
def calc_taxable(agi, deduction):
    taxable = agi - deduction
    if taxable < 0:
        taxable = 0
    return taxable

# Calculate tax for single or dependent
def calc_tax(status, taxable):
    # Married
    if status == 2:
        if taxable > 80000:
            tax = (taxable-80000) * TWENTY_TWO_PCT + 9200
        elif taxable > 20000:
            tax = (taxable-20000) * TWELVE_PCT + 2000
        else:
            tax = taxable * TEN_PCT
    # Single or dependent
    else:
        if taxable > 85000:
            tax = (taxable-85000) * TWENTY_FOUR_PCT + 14500
        elif taxable > 40000:
            tax = (taxable-40000) * TWENTY_TWO_PCT + 4600
        elif taxable > 10000:
            tax = (taxable-10000) * TWELVE_PCT + 1000
        else:
            tax = taxable * TEN_PCT
    tax = round(tax)
    return int(tax)

# Calculate tax due and check for negative withheld
def calc_tax_due(tax, withheld):
    if withheld < 0:
        withheld = 0
    due = tax - withheld
    return due

# Start the main program
if __name__ == '__main__':

    # Step 1: Get input from user
    #
    # my_inputs will be a list of integers with 5 elements
    #
    # If the input line is "10000 500 1000 1 2000"
    # my_inputs will be [10000, 500, 1000, 1, 2000]
    #
    my_inputs = [int(i) for i in input().split()]

    my_wages = my_inputs[0]
    my_interest = my_inputs[1]
    my_unemployment = my_inputs[2]
    my_status = my_inputs[3]
    my_withheld = my_inputs[4]

    # Step 2: Calculate AGI
    my_agi = calc_AGI(my_wages, my_interest, my_unemployment)

    # Step 3: Calculate Deduction
    my_deduction = get_deduction(my_status)

    # Step 4: Calculate taxable income
    my_taxable = calc_taxable(my_agi, my_deduction)

    # Step 5: Calculate tax
    my_tax = calc_tax(my_status, my_taxable)

    # Step 6: Calculate tax due
    my_due = calc_tax_due(my_tax, my_withheld)

    # Step 7: Print report
    print(f"AGI: ${my_agi:,}")
    print(f"Deduction: ${my_deduction:,}")
    print(f"Taxable income: ${my_taxable:,}")
    print(f"Federal tax: ${my_tax:,}")
    print(f"Tax due: ${my_due:,}")
