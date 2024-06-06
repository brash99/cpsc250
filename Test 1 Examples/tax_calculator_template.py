# Calculate AGI and repair any negative values
def calc_AGI(wages, interest, unemployment):
    agi = abs(wages) + abs(interest) + abs(unemployment)
    return agi

# Calculate deduction depending on single, dependent or married
def get_deduction(status):
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

    if status == 2:

        if taxable > 80000:
            tax = (taxable-80000) * 0.22 + 9200
        elif taxable > 20000:
            tax = (taxable-20000) * 0.12 + 2000
        else:
            tax = taxable * 0.10

    else:

        if taxable > 85000:
            tax = (taxable-85000) * 0.24 + 14500
        elif taxable > 40000:
            tax = (taxable-40000) * 0.22 + 4600
        elif taxable > 10000:
            tax = (taxable-10000) * 0.12 + 1000
        else:
            tax = taxable * 0.10

    tax = int(round(tax))
    return tax

# Calculate tax due and check for negative withheld
def calc_tax_due(tax, withheld):
    if withheld < 0:
        withheld = 0

    tax_due = tax - withheld
    return tax_due

if __name__ == '__main__':
    # Step #1: Input wages, interest, unemployment, status, withheld

    wages, interest, unemployment, status, withheld = \
        [int(x) for x in input().split()]

    # Step #2: Calculate AGI
    agi = calc_AGI(wages, interest, unemployment)

    # Step #3: Calculate deduction
    deduction = get_deduction(status)

    # Step #4: Calculate taxable income
    taxable_income = calc_taxable(agi, deduction)

    # Step #5: Calculate tax
    # This is the most difficult part of the program
    tax = calc_tax(status, taxable_income)

    # Step #6: Calculate tax due
    tax_due = calc_tax_due(tax, withheld)

    # Step #7: Print report
    print(f"AGI: ${agi:,}")
    print(f"Deduction: ${deduction:,}")
    print(f"Taxable income: ${taxable_income:,}")
    print(f"Federal Tax: ${tax:,}")
    print(f"Tax due: ${tax_due:,}")
