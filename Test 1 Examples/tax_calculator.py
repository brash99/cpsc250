TEN_PCT = 0.1
TWELVE_PCT = 0.12
TWENTY_TWO_PCT = 0.22
TWENTY_FOUR_PCT = 0.24

# Calculate AGI and repair any negative values
def calc_AGI(wages, interest, unemployment):
    agi = abs(wages)
    agi += abs(interest)
    agi += abs(unemployment)
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

if __name__ == '__main__':

    # Step 1: Get input
    wages, interest, unemployment, status, withheld = [
        int(val) for val in input().split()
    ]

    # Step 2: Calculate AGI
    agi = calc_AGI(wages, interest, unemployment)


    # Step 3: Calculate Deduction
    deduction = get_deduction(status)

    # Step 4: Calculate taxable income
    taxable = calc_taxable(agi, deduction)

    # Step 5: Calculate tax
    tax = calc_tax(status, taxable)

    # Step 6: Calculate tax due
    due = calc_tax_due(tax, withheld)

    # Step 7: Print report
    print(f"AGI: ${agi:,}")
    print(f"Deduction: ${deduction:,}")
    print(f"Taxable income: ${taxable:,}")
    print(f"Federal tax: ${tax:,}")
    print(f"Tax due: ${due:,}")
